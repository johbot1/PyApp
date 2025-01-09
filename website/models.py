#Models.py
#Author: John Botonakis
#With help from "Tech With Tim" on Youtube
#Desc:

from . import db
from flask_login import UserMixin #Custom inheritance class used for User objects
from sqlalchemy.sql import func

#Note:
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime(timezone = True), default = func.now, nullable=False)

#User:
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) #Defines column and Primary Key for database
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, index=True)
    password = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(128))