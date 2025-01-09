#Init.py
#Author: John Botonakis
#With help from "Tech With Tim" on Youtube
#Desc:

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "<6178357>"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}" #Stores database inside of Website folder
    db.init_app(app) #Initializes database


    from .views import views
    from .auth import auth
    #Defines prefixes for website naviagtion
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app