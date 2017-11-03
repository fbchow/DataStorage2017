from flask import Flask, render_template, request
from models import db, Transportation
import json
from collections import defaultdict

app = Flask(__name__)

POSTGRES = {
    'user': 'postgres',
    'pw': 'postgres',
    'db': 'postgres',
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
    row = Transportation.query.get('0500000US12001')
    
    # testDist = [['Mode of Transportation','%' ],
    #             ['car',row.HC01_EST_VC03 ],
    #             ['Drove Alone',row.HC01_EST_VC04 ],
    #             ['Carpooled',row.HC01_EST_VC05 ],
    #             ['2 Person Carpool',row.HC01_EST_VC06 ],
    #             ['3 Person Carpool',row.HC01_EST_VC06 ],
    #             ['4+ Person Carpool',row.HC01_EST_VC08 ],
    #             ['Workers per car',row.HC01_EST_VC09 ],
    #             ['Public Transportation',row.HC01_EST_VC10 ],
    #             ['Walked',row.HC01_EST_VC11 ],
    #             ['Bicycle',row.HC01_EST_VC12 ],
    #             ['Taxi, Motorcycle, Other',row.HC01_EST_VC13 ]
    # ]

   
    # payload = json.dumps(testDist)
  


    return render_template('views/index.html', data=row)


@app.route("/line")
def line():
    # USpop = Transportation.query.filter(Transportation.geo_id=="0100000US", Transportation.year==2010)
    datadict = defaultdict(dict)
    rows = Transportation.query.all()
    for row in rows:
        if row.hc01_est_vc01 != "null" and row.hc01_est_vc01 is not None:
            datadict[row.geo_id][row.year] = float(row.hc01_est_vc01)
        else:
            datadict[row.geo_id][row.year] = 0

    return render_template('views/line.html',datadict=datadict)

@app.route("/topfive")
def scattertopfive():
    # USpop = Transportation.query.filter(Transportation.geo_id=="0100000US", Transportation.year==2010)
    datadict2 = defaultdict(dict)
    rows = Transportation.query.all()
    for row in rows:
        if row.hc01_est_vc01 != "null" and row.hc01_est_vc01 is not None:
            datadict2[row.geo_id][row.year] = float(row.hc01_est_vc01)
        else:
            datadict2[row.geo_id][row.year] = 0

    return render_template('views/scattertopfive.html',datadict2=datadict2)

@app.route("/commute")
def commute():
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

    return render_template('views/commutetime.html',datadict3=datadict3)

@app.route("/genderbiking")
def biking():
    genderbiking16 = Transportation.query.filter(Transportation.year == 2016)
    bikingdict = defaultdict(dict)
    for county in genderbiking16:
        if county.hc02_est_vc12 != "null" and county.hc02_est_vc12 is not None and county.hc03_est_vc12 != "null" and county.hc03_est_vc12 is not None:
            fem = float(county.hc03_est_vc12)
            male = float(county.hc02_est_vc12)
            maxbiking = max(male,fem)
            bikingdict[county.geo_id] = ((male-fem)/maxbiking)

    return render_template('views/genderbiking.html',bikingdict=bikingdict)

@app.route("/merge")
def mergeline():
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

    return render_template('views/merge.html', datadict = datadict, datadict3=datadict3, bikingdict=bikingdict)
#------------------------
# Launcher `~=}}}}>
#------------------------

if __name__ == '__main__':
    app.run()