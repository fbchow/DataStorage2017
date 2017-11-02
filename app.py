from flask import Flask, render_template, request
from models import db, Transportation
import json

app = Flask(__name__)

POSTGRES = {
    'user': 'postgres',
    'pw': 'postgres',
    'db': 'usTransportation',
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
    
    testDist = [['Mode of Transportation','%' ],
                ['car',row.HC01_EST_VC03 ],
                ['Drove Alone',row.HC01_EST_VC04 ],
                ['Carpooled',row.HC01_EST_VC05 ],
                ['2 Person Carpool',row.HC01_EST_VC06 ],
                ['3 Person Carpool',row.HC01_EST_VC06 ],
                ['4+ Person Carpool',row.HC01_EST_VC08 ],
                ['Workers per car',row.HC01_EST_VC09 ],
                ['Public Transportation',row.HC01_EST_VC10 ],
                ['Walked',row.HC01_EST_VC11 ],
                ['Bicycle',row.HC01_EST_VC12 ],
                ['Taxi, Motorcycle, Other',row.HC01_EST_VC13 ]
    ]

   
    payload = json.dumps(testDist)
  


    return render_template('views/index.html', data=payload)



#------------------------
# Launcher `~=}}}}>
#------------------------

if __name__ == '__main__':
    app.run()