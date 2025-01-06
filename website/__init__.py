from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "<6178357>"


    from .views import views
    from .auth import auth
    #Defines prefixes for website naviagtion
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app