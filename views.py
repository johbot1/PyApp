#Views.py
#Author: John Botonakis
#Desc:

from flask import Blueprint, render_template,request,jsonify,redirect,url_for

#Routing template: __name__, name of import
views = Blueprint( __name__,'views')

@views.route('/')
def indexHome():
    return render_template("index.html")

@views.route('/about')
def about():
    return "About Page!"

#Getting variables/parameters in URL
@views.route('/profile')
def profile():
    args = request.args
    name = args.get('name')
    return render_template("index.html",name = name)

#How to inlcude JSON
@views.route('/json')
def get_json():
    return jsonify({'name':'Tim','coolness':10})

#How to get requests
@views.route('/data')
def get_data():
    data = request.json
    return jsonify(data)

#How to redirect
@views.route('/go-to-home')
def go_to_home():
    return redirect(url_for('views.home'))

