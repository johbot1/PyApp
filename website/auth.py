# Auth.py
# Author: John Botonakis
# With some help from "Tech With Tim" on YouTube
# Desc:
# This file handles the routes related to authentication,
# including login, logout, and signup.
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from . import db
from .models import User

# Create a Blueprint for the authentication routes
# A Blueprint is a template for generating a section of a web app
# similar to a casting mold.
auth = Blueprint('auth', __name__)


# Route: Login
# Gathers the input from the fields and compares it with a temporary user object.
# It searches the database to ensure the account with the provided email exists,
# then compares the passwords, giving visual feedback if either do not match.
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email_login')
        password = request.form.get('loginpass_login')

        user = User.query.filter_by(email=email).first()
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
# Redirect for when the user logs out of their account
@auth.route('/logout')
@login_required  # Cannot log out unless you're logged in.
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


# Route: Signup
# Handles account registration and User creation. Once information is gathered,
# it validates the input, then creates and adds a User object to the database
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        # Retrieves inputs from the signup form
        # Local_name = request.form.get('input_name_in_html_sheet')
        email = request.form.get('email_signup')
        first_name = request.form.get('firstname_signup')
        password1 = request.form.get('pass1_signup')
        password2 = request.form.get('pass2_signup')

        # Input Validation
        # Creates a temporary user object as a query to ensure the email is not
        # currently already in use. Then checks name and password match before
        # adding the user to the database.
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email Already Exists!", category="error")
        elif len(email) < 4:
            flash("Email must be at least 4 characters or greater", category="error")
        elif len(first_name) < 3:
            flash("First Name must be at least 3 characters or greater", category="error")
        elif password1 != password2:
            flash("Your passwords don't match!", category="error")
        elif len(password1) < 7:
            flash("Password must be at least 7 characters or greater", category="error")
        else:
            # Creates a new user with the parameters specified,
            # Encrypts the password using werkzeug.security import
            # Adds the new user, commits to database, and logs them in
            new_user = User(
                email=email,
                username=first_name,
                password=generate_password_hash(password1, method='scrypt'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash("Account Created Successfully!", category="success")
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)  # Renders the signup page
