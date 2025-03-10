# Models.py
# Author: John Botonakis
# With some help from "Tech With Tim" on YouTube
# Desc:
# This defines the database models for the web app using SQLAlchemy.
# It includes models for `Note` and `User`, defining their attributes and relationships.
from flask_login import UserMixin  # Custom inheritance class used for User objects
from sqlalchemy.sql import func

from . import db


# Note Model:
# Represents text written by users, saved as a Note. Each Note has an ID, text data, and a timestamp
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each note (Primary Key)
    data = db.Column(db.String(200), nullable=False)  # The content of the note, which cannot be empty
    date = db.Column(
        db.DateTime(timezone=True),
        default=func.now,
        nullable=False)  # Timestamp for when the note was created, defaults to current time
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'))  # References user.id as ForeignKey to link notes to users


# User:
# Represents a User object, with their own ID, email, username, and password
# UserMixin is needed for compatability with current_user module of flask_login
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each user (Primary Key)
    email = db.Column(
        db.String(100),
        unique=True,
        nullable=False)  # Email address of the user, must be unique and non-empty
    username = db.Column(
        db.String(100),
        unique=True,
        index=True)  # Username of the user, must be unique and indexed for faster queries
    password = db.Column(
        db.String(100),
        nullable=False)
    notes = db.relationship("Note")  # Relates the user created notes back to the Notes database
