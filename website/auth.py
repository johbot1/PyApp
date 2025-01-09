#Auth.py
#Author: John Botonakis
#With help from "Tech With Tim" on Youtube
#Desc:

from flask import Blueprint, render_template, request,flash

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
    if request.method == "POST":
        email = request.form.get('email_input')
        first_name = request.form.get('firstname_input')
        password1 = request.form.get('pass1_input')
        password2 = request.form.get('pass2_input')

        if len(email) < 4:
            flash("Email must be at least 4 characters or greater", category="error")
        elif len (first_name) < 3:
            flash("First Name must be at least 3 characters or greater", category="error")
        elif password1 != password2:
            flash("Your passwords don't match!", category="error")
        elif len(password1) < 7:
            flash("Password must be at least 7 characters or greater", category="error")
        else:
            #add the user
            flash("Success! Account Created!", category="success")

    return render_template("signup.html")