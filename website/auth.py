#Auth.py
#Author: John Botonakis
#With help from "Tech With Tim" on Youtube
#Desc:

from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p> Login </p>"

@auth.route('/logout')
def logout():
    return "<p> Logout </p>"

@auth.route('/signup')
def signup():
    return "<p> Sign up </p>"