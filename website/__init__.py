#Init.py
#Author: John Botonakis
#With help from "Tech With Tim" on Youtube
#Desc:
#This file initializes the Flask application, sets up the database, and registers the blueprints for routing.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


# Initialize the SQLAlchemy database object
db = SQLAlchemy()
# Name of the SQLite database file
DB_NAME = "database.db"

# Function to create and configure the Flask application
def create_app():
    # Create a Flask app instance
    app = Flask(__name__)

    # Set a secret key for the session
    app.config["SECRET_KEY"] = "<6178357>"

    # Configure the app to use an SQLite database stored in the project directory
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"

    # Initialize the SQLAlchemy database object with the Flask app
    db.init_app(app)

    # Import and register blueprints for routing
    from .views import views
    from .auth import auth

    # Register the 'views' blueprint with no URL prefix
    app.register_blueprint(views, url_prefix="/")

    # Register the 'auth' blueprint with no URL prefix
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Note

    create_db(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    #How to load a user
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

#Using OS.path, check to see if the DB exists.
#If not, create it and confirm it with a printout
def create_db(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Database created successfully")