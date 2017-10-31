# import sqlalchemy class
from flask_sqlalchemy import SQLAlchemy

# create instance of sqlalchemy class
db = SQLAlchemy()

# create python class to define relational db of our postgres db
# start defining classes for our postgres database here!

# class User(db.Model):
#     __tablename__ = 'users'
#     uid = db.Column(db.Integer, primary_key = True)
#     firstname = db.Column(db.String(100))
#     lastname = db.Column(db.String(100))
#     email = db.Column(db.String(120), unique=True)
#     pwdhash = db.Column(db.String(54))
