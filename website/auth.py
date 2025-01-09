#Auth.py
#Author: John Botonakis
#With help from "Tech With Tim" on Youtube
#Desc:
# This file handles the routes related to authentication, including login, logout, and signup.
from flask import Blueprint, render_template, request,flash,redirect,url_for
from .models import User
from flask_login import login_user,logout_user,login_required,current_user
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

# Create a Blueprint for the authentication routes
auth = Blueprint('auth', __name__)

# Route: Login
# Handles both GET and POST requests for the login page.
@auth.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
     email = request.form.get('email')
     password = request.form.get('password')

     user = User.query.filter_by(email_login = email).first()
     if user:
         if check_password_hash(user.password, password):
             flash('Logged in successfully!', category='success')
             login_user(user, remember=True)
             return redirect(url_for('views.home'))
         else:
             flash('Login Unsuccessful! Check your email/password combination', category='error')
     else:
         flash('Login Unsuccessful! Email does not exist.', category='error')

   return render_template("login.html", user=current_user)

# Route: Logout
# Placeholder route for user logout.
@auth.route('/logout')
@login_required #Cannot access this page unless you're logged in.
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# Route: Signup
# Handles user registration with GET and POST methods.
@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == "POST":
        # Retrieves inputs from the signup form
        email = request.form.get('email_signup')
        first_name = request.form.get('firstname_signup')
        password1 = request.form.get('pass1_signup')
        password2 = request.form.get('pass2_signup')

        user = User.query.filter_by(email=email).first()
        #Input Validation
        #TODO: Could this be shrunk into it's own function?
        if user:
            flash("Email Already Exists!", category="error")
        elif len(email) < 4:
            flash("Email must be at least 4 characters or greater", category="error")
        elif len (first_name) < 3:
            flash("First Name must be at least 3 characters or greater", category="error")
        elif password1 != password2:
            flash("Your passwords don't match!", category="error")
        elif len(password1) < 7:
            flash("Password must be at least 7 characters or greater", category="error")
        else:
            #add the user
            new_user = User(
                email = email,
                username = first_name,
                password = generate_password_hash(password1, method = 'scrypt'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash("Account Created Successfully!", category="success")
            return redirect(url_for('views.home'))

    return render_template("signup.html",user = current_user)# Renders the signup page