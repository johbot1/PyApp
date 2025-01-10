# Init.py
# Author: John Botonakis
# With some help from "Tech With Tim" on YouTube
# Desc:
# This file initializes the Flask application, sets up
# the database, and registers the blueprints for routing.
from os import path

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy database object as db
db = SQLAlchemy()
# Name of the SQLite database file
DB_NAME = "database.db"


# This function creates the web app by beginning a Flask app,
# configuring its database, registering its blueprints and
# loading its users.
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

    # Import the User and Note classes. Done here, as opposed to
    # outside of this loop, to better
    from .models import User, Note

    # Creates the database using the 'app' as contextual argument
    create_db(app)

    # Using flask_login, creates a login manager that will
    # save the settings for logging a user in. It is told to look
    # for login information by being pointed to 'auth.login'.
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # Using flask_login as a Login Manager to get the current user ID
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


# Using OS.path, check to see if the DB exists.
# If not, create it with the app argument as context,
# and confirm it with a printout. App context is needed to avoid
# circuluar logic issues, and used instead of passing 'app' to each function.
def create_db(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Database created successfully")
