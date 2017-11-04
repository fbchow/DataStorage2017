from flask import Flask, render_template, request
from models import db, Transportation
import json
from collections import defaultdict

app = Flask(__name__)

POSTGRES = {
    'user': 'khunt',
# replace pw
    'pw': '#####',
    'db': 'khunt',
    'host': 'localhost',
    'port': '5432',
}

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db.init_app(app)

#------------------------
# Controllers ;)
#------------------------

@app.route("/")
def main():
    # USpop = Transportation.query.filter(Transportation.geo_id=="0100000US", Transportation.year==2010)
    datadict = defaultdict(dict)
    rows = Transportation.query.all()
    for row in rows:
        if row.hc01_est_vc01 != "null" and row.hc01_est_vc01 is not None:
            datadict[row.geo_id][row.year] = float(row.hc01_est_vc01)
        else:
            datadict[row.geo_id][row.year] = 0

    

    commutes = Transportation.query.filter((Transportation.geo_id=="0100000US") |
    (Transportation.geo_id=='0400000US12') | (Transportation.geo_id=='0500000US12021') | 
    (Transportation.geo_id=='0500000US12071') | (Transportation.geo_id=='0500000US12081') |
    (Transportation.geo_id=='0500000US12109') | (Transportation.geo_id=='0500000US12097'))
    datadict3 = defaultdict(dict)
    for commute in commutes:
        if commute.hc01_est_vc55 != "null" and commute.hc01_est_vc55 is not None:
            datadict3[commute.geo_id][commute.year] = float(commute.hc01_est_vc55)
        else:
            datadict3[commute.geo_id][commute.year] = 0

    

    genderbiking16 = Transportation.query.filter(Transportation.year == 2016)
    bikingdict = defaultdict(dict)
    for county in genderbiking16:
        if county.hc02_est_vc12 != "null" and county.hc02_est_vc12 is not None and county.hc03_est_vc12 != "null" and county.hc03_est_vc12 is not None:
            fem = float(county.hc03_est_vc12)
            male = float(county.hc02_est_vc12)
            maxbiking = max(male,fem)
            bikingdict[county.geo_id] = ((male-fem)/maxbiking)
    
    eco = defaultdict(dict)
    ecorows = Transportation.query.all()
    for ecorow in ecorows:
        a = ecorow.hc01_est_vc04
        b = ecorow.hc01_est_vc10
        c = ecorow.hc01_est_vc11
        if  a != "null" and b != "null" and c != "null" and a is not None and b is not None and c is not None:
            eco[ecorow.geo_id][ecorow.year] = float(ecorow.hc01_est_vc04) + float(ecorow.hc01_est_vc10) + float(ecorow.hc01_est_vc11)
        else:
            eco[ecorow.geo_id][ecorow.year] = 0

    return render_template('views/merge.html', datadict = datadict, datadict3=datadict3, bikingdict=bikingdict, eco=eco)
#------------------------
# Launcher `~=}}}}>
#------------------------

if __name__ == '__main__':
    app.run()
