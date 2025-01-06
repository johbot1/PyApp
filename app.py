#App.py
#Author: John Botonakis
#Desc:
from flask import Flask

from views import views

app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Welcome to this web app!"
app.register_blueprint(views, url_prefix='/')
# app.register_blueprint(views, url_prefix='/home')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
