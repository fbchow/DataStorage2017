from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
        """
                Define a base way to jsonify models, dealing with datetime objects
        """
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }


class Transportation(BaseModel, db.Model):
    """Model for the stations table"""
    __tablename__ = 'acs_data2016'
    # geo_id = db.Column(db.String(100), primary_key = True)
    geo_id = db.Column(db.String(100), primary_key=True)
    geo_id2 = db.Column(db.String(100))
    year = db.Column(db.Integer, primary_key=True)
    geo_display_label  = db.Column(db.String(100))
    hc01_est_vc01 = db.Column(db.String(100)) # number workers > 16
    hc01_est_vc03 = db.Column(db.String(100))
    hc01_est_vc04 = db.Column(db.String(100))
    hc01_est_vc05 = db.Column(db.String(100))
    hc01_est_vc10 = db.Column(db.String(100))
    hc01_est_vc11 = db.Column(db.String(100))
    hc01_est_vc12 = db.Column(db.String(100))
    hc02_est_vc12 = db.Column(db.String(100))
    hc03_est_vc12 = db.Column(db.String(100))
    hc01_est_vc13 = db.Column(db.String(100))
    hc01_est_vc14 = db.Column(db.String(100))
    hc01_est_vc34 = db.Column(db.String(100))
    hc01_est_vc35 = db.Column(db.String(100))
    hc01_est_vc36 = db.Column(db.String(100))
    hc01_est_vc37 = db.Column(db.String(100))
    hc01_est_vc38 = db.Column(db.String(100))
    hc01_est_vc39 = db.Column(db.String(100))
    hc01_est_vc40 = db.Column(db.String(100))
    hc01_est_vc41 = db.Column(db.String(100))
    hc01_est_vc42 = db.Column(db.String(100))
    hc01_est_vc43 = db.Column(db.String(100))
    hc01_est_vc46 = db.Column(db.String(100))
    hc01_est_vc47 = db.Column(db.String(100))
    hc01_est_vc48 = db.Column(db.String(100))
    hc01_est_vc49 = db.Column(db.String(100))
    hc01_est_vc50 = db.Column(db.String(100))
    hc01_est_vc51 = db.Column(db.String(100))
    hc01_est_vc52 = db.Column(db.String(100))
    hc01_est_vc53 = db.Column(db.String(100))
    hc01_est_vc54 = db.Column(db.String(100))
    hc01_est_vc55 = db.Column(db.String(100))


    '''
    HC01_EST_VC23	HC01_MOE_VC23	HC02_EST_VC23	HC02_MOE_VC23	HC03_EST_VC23	HC03_MOE_VC23	HC01_EST_VC24	HC01_MOE_VC24	HC02_EST_VC24	HC02_MOE_VC24	HC03_EST_VC24	HC03_MOE_VC24	HC01_EST_VC25	HC01_MOE_VC25	HC02_EST_VC25	HC02_MOE_VC25	HC03_EST_VC25	HC03_MOE_VC25	HC01_EST_VC32	HC01_MOE_VC32	HC02_EST_VC32	HC02_MOE_VC32	HC03_EST_VC32	HC03_MOE_VC32	HC01_EST_VC34	HC01_MOE_VC34	HC02_EST_VC34	HC02_MOE_VC34	HC03_EST_VC34	HC03_MOE_VC34	HC01_EST_VC35	HC01_MOE_VC35	HC02_EST_VC35	HC02_MOE_VC35	HC03_EST_VC35	HC03_MOE_VC35	HC01_EST_VC36	HC01_MOE_VC36	HC02_EST_VC36	HC02_MOE_VC36	HC03_EST_VC36	HC03_MOE_VC36	HC01_EST_VC37	HC01_MOE_VC37	HC02_EST_VC37	HC02_MOE_VC37	HC03_EST_VC37	HC03_MOE_VC37	HC01_EST_VC38	HC01_MOE_VC38	HC02_EST_VC38	HC02_MOE_VC38	HC03_EST_VC38	HC03_MOE_VC38	HC01_EST_VC39	HC01_MOE_VC39	HC02_EST_VC39	HC02_MOE_VC39	HC03_EST_VC39	HC03_MOE_VC39	HC01_EST_VC40	HC01_MOE_VC40	HC02_EST_VC40	HC02_MOE_VC40	HC03_EST_VC40	HC03_MOE_VC40	HC01_EST_VC41	HC01_MOE_VC41	HC02_EST_VC41	HC02_MOE_VC41	HC03_EST_VC41	HC03_MOE_VC41	HC01_EST_VC42	HC01_MOE_VC42	HC02_EST_VC42	HC02_MOE_VC42	HC03_EST_VC42	HC03_MOE_VC42	HC01_EST_VC43	HC01_MOE_VC43	HC02_EST_VC43	HC02_MOE_VC43	HC03_EST_VC43	HC03_MOE_VC43	HC01_EST_VC46	HC01_MOE_VC46	HC02_EST_VC46	HC02_MOE_VC46	HC03_EST_VC46	HC03_MOE_VC46	HC01_EST_VC47	HC01_MOE_VC47	HC02_EST_VC47	HC02_MOE_VC47	HC03_EST_VC47	HC03_MOE_VC47	HC01_EST_VC48	HC01_MOE_VC48	HC02_EST_VC48	HC02_MOE_VC48	HC03_EST_VC48	HC03_MOE_VC48	HC01_EST_VC49	HC01_MOE_VC49	HC02_EST_VC49	HC02_MOE_VC49	HC03_EST_VC49	HC03_MOE_VC49	HC01_EST_VC50	HC01_MOE_VC50	HC02_EST_VC50	HC02_MOE_VC50	HC03_EST_VC50	HC03_MOE_VC50	HC01_EST_VC51	HC01_MOE_VC51	HC02_EST_VC51	HC02_MOE_VC51	HC03_EST_VC51	HC03_MOE_VC51	HC01_EST_VC52	HC01_MOE_VC52	HC02_EST_VC52	HC02_MOE_VC52	HC03_EST_VC52	HC03_MOE_VC52	HC01_EST_VC53	HC01_MOE_VC53	HC02_EST_VC53	HC02_MOE_VC53	HC03_EST_VC53	HC03_MOE_VC53	HC01_EST_VC54	HC01_MOE_VC54	HC02_EST_VC54	HC02_MOE_VC54	HC03_EST_VC54	HC03_MOE_VC54	HC01_EST_VC55	HC01_MOE_VC55	HC02_EST_VC55	HC02_MOE_VC55	HC03_EST_VC55	HC03_MOE_VC55	HC01_EST_VC58	HC01_MOE_VC58	HC02_EST_VC58	HC02_MOE_VC58	HC03_EST_VC58	HC03_MOE_VC58	HC01_EST_VC59	HC01_MOE_VC59	HC02_EST_VC59	HC02_MOE_VC59	HC03_EST_VC59	HC03_MOE_VC59	HC01_EST_VC60	HC01_MOE_VC60	HC02_EST_VC60	HC02_MOE_VC60	HC03_EST_VC60	HC03_MOE_VC60	HC01_EST_VC61	HC01_MOE_VC61	HC02_EST_VC61	HC02_MOE_VC61	HC03_EST_VC61	HC03_MOE_VC61	HC01_EST_VC62	HC01_MOE_VC62	HC02_EST_VC62	HC02_MOE_VC62	HC03_EST_VC62	HC03_MOE_VC62	HC01_EST_VC65	HC01_EST_VC66	HC01_EST_VC67	HC01_EST_VC68	HC01_EST_VC69	HC01_EST_VC70																																																	
    '''
