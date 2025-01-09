#Views.py
#Author: John Botonakis
#With help from "Tech With Tim" on Youtube
#Desc:

from flask import Blueprint,render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)
@views.route('/')
@login_required
def home():
    return render_template("home.html")

# @views.route('/login')
# def login():
#     return render_template("login.html",user = current_user)