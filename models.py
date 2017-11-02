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
    __tablename__ = 'transportation'
    id = db.Column(db.String(100), primary_key = True)
    id2 = db.Column(db.Integer)
    disp_label = db.Column(db.String(100))
    HC01_EST_VC01 = db.Column(db.Integer)
    HC01_MOE_VC01 = db.Column(db.Integer)
    HC02_EST_VC01 = db.Column(db.Integer)
    HC02_MOE_VC01 = db.Column(db.Integer)
    HC03_EST_VC01 = db.Column(db.Integer)
    HC03_MOE_VC01 = db.Column(db.Integer)
    HC01_EST_VC03 = db.Column(db.Float)
    HC01_MOE_VC03 = db.Column(db.Float)
    HC02_EST_VC03 = db.Column(db.Float)
    HC02_MOE_VC03 = db.Column(db.Float)
    HC03_EST_VC03 = db.Column(db.Float)
    HC03_MOE_VC03 = db.Column(db.Float)
    HC01_EST_VC04 = db.Column(db.Float)
    HC01_MOE_VC04 = db.Column(db.Float)
    HC02_EST_VC04 = db.Column(db.Float)
    HC02_MOE_VC04 = db.Column(db.Float)
    HC03_EST_VC04 = db.Column(db.Float)
    HC03_MOE_VC04 = db.Column(db.Float)
    HC01_EST_VC05 = db.Column(db.Float)
    HC01_MOE_VC05 = db.Column(db.Float)
    HC02_EST_VC05 = db.Column(db.Float)
    HC02_MOE_VC05 = db.Column(db.Float)
    HC03_EST_VC05 = db.Column(db.Float)
    HC03_MOE_VC05 = db.Column(db.Float)
    HC01_EST_VC06 = db.Column(db.Float)
    HC01_MOE_VC06 = db.Column(db.Float)
    HC02_EST_VC06 = db.Column(db.Float)
    HC02_MOE_VC06 = db.Column(db.Float)
    HC03_EST_VC06 = db.Column(db.Float)
    HC03_MOE_VC06 = db.Column(db.Float)
    HC01_EST_VC07 = db.Column(db.Float)
    HC01_MOE_VC07 = db.Column(db.Float)
    HC02_EST_VC07 = db.Column(db.Float)
    HC02_MOE_VC07 = db.Column(db.Float)
    HC03_EST_VC07 = db.Column(db.Float)
    HC03_MOE_VC07 = db.Column(db.Float)
    HC01_EST_VC08 = db.Column(db.Float)
    HC01_MOE_VC08 = db.Column(db.Float)
    HC02_EST_VC08 = db.Column(db.Float)
    HC02_MOE_VC08 = db.Column(db.Float)
    HC03_EST_VC08 = db.Column(db.Float)
    HC03_MOE_VC08 = db.Column(db.Float)
    HC01_EST_VC09 = db.Column(db.Float)
    HC01_MOE_VC09 = db.Column(db.Float)
    HC02_EST_VC09 = db.Column(db.Float)
    HC02_MOE_VC09 = db.Column(db.Float)
    HC03_EST_VC09 = db.Column(db.Float)
    HC03_MOE_VC09 = db.Column(db.Float)
    HC01_EST_VC10 = db.Column(db.Float)
    HC01_MOE_VC10 = db.Column(db.Float)
    HC02_EST_VC10 = db.Column(db.Float)
    HC02_MOE_VC10 = db.Column(db.Float)
    HC03_EST_VC10 = db.Column(db.Float)
    HC03_MOE_VC10 = db.Column(db.Float)
    HC01_EST_VC11 = db.Column(db.Float)
    HC01_MOE_VC11 = db.Column(db.Float)
    HC02_EST_VC11 = db.Column(db.Float)
    HC02_MOE_VC11 = db.Column(db.Float)
    HC03_EST_VC11 = db.Column(db.Float)
    HC03_MOE_VC11 = db.Column(db.Float)
    HC01_EST_VC12 = db.Column(db.Float)
    HC01_MOE_VC12 = db.Column(db.Float)
    HC02_EST_VC12 = db.Column(db.Float)
    HC02_MOE_VC12 = db.Column(db.Float)
    HC03_EST_VC12 = db.Column(db.Float)
    HC03_MOE_VC12 = db.Column(db.Float)
    HC01_EST_VC13 = db.Column(db.Float)
    HC01_MOE_VC13 = db.Column(db.Float)
    HC02_EST_VC13 = db.Column(db.Float)
    HC02_MOE_VC13 = db.Column(db.Float)
    HC03_EST_VC13 = db.Column(db.Float)
    HC03_MOE_VC13 = db.Column(db.Float)
    HC01_EST_VC14 = db.Column(db.Float)
    HC01_MOE_VC14 = db.Column(db.Float)
    HC02_EST_VC14 = db.Column(db.Float)
    HC02_MOE_VC14 = db.Column(db.Float)
    HC03_EST_VC14 = db.Column(db.Float)
    HC03_MOE_VC14 = db.Column(db.Float)
    HC01_EST_VC17 = db.Column(db.Float)
    HC01_MOE_VC17 = db.Column(db.Float)
    HC02_EST_VC17 = db.Column(db.Float)
    HC02_MOE_VC17 = db.Column(db.Float)
    HC03_EST_VC17 = db.Column(db.Float)
    HC03_MOE_VC17 = db.Column(db.Float)
    HC01_EST_VC18 = db.Column(db.Float)
    HC01_MOE_VC18 = db.Column(db.Float)
    HC02_EST_VC18 = db.Column(db.Float)
    HC02_MOE_VC18 = db.Column(db.Float)
    HC03_EST_VC18 = db.Column(db.Float)
    HC03_MOE_VC18 = db.Column(db.Float)
    HC01_EST_VC19 = db.Column(db.Float)
    HC01_MOE_VC19 = db.Column(db.Float)
    HC02_EST_VC19 = db.Column(db.Float)
    HC02_MOE_VC19 = db.Column(db.Float)
    HC03_EST_VC19 = db.Column(db.Float)
    HC03_MOE_VC19 = db.Column(db.Float)
    HC01_EST_VC20 = db.Column(db.Float)
    HC01_MOE_VC20 = db.Column(db.Float)
    HC02_EST_VC20 = db.Column(db.Float)
    HC02_MOE_VC20 = db.Column(db.Float)
    HC03_EST_VC20 = db.Column(db.Float)
    HC03_MOE_VC20 = db.Column(db.Float)
    HC01_EST_VC22 = db.Column(db.Float)
    HC01_MOE_VC22 = db.Column(db.Float)
    HC02_EST_VC22 = db.Column(db.Float)
    HC02_MOE_VC22 = db.Column(db.Float)
    HC03_EST_VC22 = db.Column(db.Float)
    HC03_MOE_VC22 = db.Column(db.Float)

    '''
    HC01_EST_VC23	HC01_MOE_VC23	HC02_EST_VC23	HC02_MOE_VC23	HC03_EST_VC23	HC03_MOE_VC23	HC01_EST_VC24	HC01_MOE_VC24	HC02_EST_VC24	HC02_MOE_VC24	HC03_EST_VC24	HC03_MOE_VC24	HC01_EST_VC25	HC01_MOE_VC25	HC02_EST_VC25	HC02_MOE_VC25	HC03_EST_VC25	HC03_MOE_VC25	HC01_EST_VC32	HC01_MOE_VC32	HC02_EST_VC32	HC02_MOE_VC32	HC03_EST_VC32	HC03_MOE_VC32	HC01_EST_VC34	HC01_MOE_VC34	HC02_EST_VC34	HC02_MOE_VC34	HC03_EST_VC34	HC03_MOE_VC34	HC01_EST_VC35	HC01_MOE_VC35	HC02_EST_VC35	HC02_MOE_VC35	HC03_EST_VC35	HC03_MOE_VC35	HC01_EST_VC36	HC01_MOE_VC36	HC02_EST_VC36	HC02_MOE_VC36	HC03_EST_VC36	HC03_MOE_VC36	HC01_EST_VC37	HC01_MOE_VC37	HC02_EST_VC37	HC02_MOE_VC37	HC03_EST_VC37	HC03_MOE_VC37	HC01_EST_VC38	HC01_MOE_VC38	HC02_EST_VC38	HC02_MOE_VC38	HC03_EST_VC38	HC03_MOE_VC38	HC01_EST_VC39	HC01_MOE_VC39	HC02_EST_VC39	HC02_MOE_VC39	HC03_EST_VC39	HC03_MOE_VC39	HC01_EST_VC40	HC01_MOE_VC40	HC02_EST_VC40	HC02_MOE_VC40	HC03_EST_VC40	HC03_MOE_VC40	HC01_EST_VC41	HC01_MOE_VC41	HC02_EST_VC41	HC02_MOE_VC41	HC03_EST_VC41	HC03_MOE_VC41	HC01_EST_VC42	HC01_MOE_VC42	HC02_EST_VC42	HC02_MOE_VC42	HC03_EST_VC42	HC03_MOE_VC42	HC01_EST_VC43	HC01_MOE_VC43	HC02_EST_VC43	HC02_MOE_VC43	HC03_EST_VC43	HC03_MOE_VC43	HC01_EST_VC46	HC01_MOE_VC46	HC02_EST_VC46	HC02_MOE_VC46	HC03_EST_VC46	HC03_MOE_VC46	HC01_EST_VC47	HC01_MOE_VC47	HC02_EST_VC47	HC02_MOE_VC47	HC03_EST_VC47	HC03_MOE_VC47	HC01_EST_VC48	HC01_MOE_VC48	HC02_EST_VC48	HC02_MOE_VC48	HC03_EST_VC48	HC03_MOE_VC48	HC01_EST_VC49	HC01_MOE_VC49	HC02_EST_VC49	HC02_MOE_VC49	HC03_EST_VC49	HC03_MOE_VC49	HC01_EST_VC50	HC01_MOE_VC50	HC02_EST_VC50	HC02_MOE_VC50	HC03_EST_VC50	HC03_MOE_VC50	HC01_EST_VC51	HC01_MOE_VC51	HC02_EST_VC51	HC02_MOE_VC51	HC03_EST_VC51	HC03_MOE_VC51	HC01_EST_VC52	HC01_MOE_VC52	HC02_EST_VC52	HC02_MOE_VC52	HC03_EST_VC52	HC03_MOE_VC52	HC01_EST_VC53	HC01_MOE_VC53	HC02_EST_VC53	HC02_MOE_VC53	HC03_EST_VC53	HC03_MOE_VC53	HC01_EST_VC54	HC01_MOE_VC54	HC02_EST_VC54	HC02_MOE_VC54	HC03_EST_VC54	HC03_MOE_VC54	HC01_EST_VC55	HC01_MOE_VC55	HC02_EST_VC55	HC02_MOE_VC55	HC03_EST_VC55	HC03_MOE_VC55	HC01_EST_VC58	HC01_MOE_VC58	HC02_EST_VC58	HC02_MOE_VC58	HC03_EST_VC58	HC03_MOE_VC58	HC01_EST_VC59	HC01_MOE_VC59	HC02_EST_VC59	HC02_MOE_VC59	HC03_EST_VC59	HC03_MOE_VC59	HC01_EST_VC60	HC01_MOE_VC60	HC02_EST_VC60	HC02_MOE_VC60	HC03_EST_VC60	HC03_MOE_VC60	HC01_EST_VC61	HC01_MOE_VC61	HC02_EST_VC61	HC02_MOE_VC61	HC03_EST_VC61	HC03_MOE_VC61	HC01_EST_VC62	HC01_MOE_VC62	HC02_EST_VC62	HC02_MOE_VC62	HC03_EST_VC62	HC03_MOE_VC62	HC01_EST_VC65	HC01_EST_VC66	HC01_EST_VC67	HC01_EST_VC68	HC01_EST_VC69	HC01_EST_VC70																																																	
    '''
