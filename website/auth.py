#App.py
#Author: John Botonakis
#With help from "Tech With Tim" on Youtube
#Desc:

from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/home')
def home():
    return render_template("home.html")

#This method can accept GET and POST requests
@auth.route('/login', methods = ['GET', 'POST'])
def login():
    data = request.form #Contains information relating to the request that was sent to access this route
    print (data)
    return render_template("login.html", text = "User is True", boolean = False)

@auth.route('/logout')
def logout():
    return "<p> Logout </p>"

#This method can accept GET and POST requests
@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    data = request.form
    return render_template("signup.html")