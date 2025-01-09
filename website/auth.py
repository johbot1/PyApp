#Auth.py
#Author: John Botonakis
#With help from "Tech With Tim" on Youtube
#Desc:
# This file handles the routes related to authentication, including login, logout, and signup.
from flask import Blueprint, render_template, request,flash

# Create a Blueprint for the authentication routes
auth = Blueprint('auth', __name__)

# Route: Home
# This route renders the home page.
@auth.route('/home')
def home():
    return render_template("home.html")

# Route: Login
# Handles both GET and POST requests for the login page.
@auth.route('/login', methods = ['GET', 'POST'])
def login():
    data = request.form #Contains information relating to the request that was sent to access this route
    print (data)
    return render_template("login.html", text = "User is True", boolean = False)

# Route: Logout
# Placeholder route for user logout.
@auth.route('/logout')
def logout():
    return "<p> Logout </p>"

# Route: Signup
# Handles user registration with GET and POST methods.
@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == "POST":
        # Retrieves inputs from the signup form
        email = request.form.get('email_input')
        first_name = request.form.get('firstname_input')
        password1 = request.form.get('pass1_input')
        password2 = request.form.get('pass2_input')
        #Input Validation
        #TODO: Could this be shrunk into it's own function?
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

    return render_template("signup.html")# Renders the signup page