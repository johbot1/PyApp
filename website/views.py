# Views.py
# Author: John Botonakis
# With some help from "Tech With Tim" on YouTube
# Desc:
# Stores routes for user navigation. Any place a user can go to is through views.py
# This is different from auth.py, because it does not handle any authentication
import json
from datetime import datetime

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user

from . import db
from .models import Note

# Creates a Blueprint for each unique view route.
# A Blueprint is a template for generating a section of a web app
# similar to a casting mold.
views = Blueprint('views', __name__)


# Route: Home
# The home page users will see when logging in. They are able to enter in information into a 'note'
# object, which is then ingested, added, and committed to the database for later retrieval.
# The logic in here is self-explanatory.
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('Note')
        if len(note) < 3:
            flash('Note must be at least 3 characters!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id, date=datetime.now())
            db.session.add(new_note)
            db.session.commit()
            flash('Note successfully added!', category='success')

    return render_template("home.html", user=current_user)


# Route: Delete Note
# When deleting a note, this route is called to gather the note deletion request,
# get the note ID, confirm that the note was made by the user logged in, then delete it
# and update the database. It then returns an empty response to the calling function to continue it.
@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)  # Get the note deletion request
    noteId = note['noteId']  # Convert to a python dictionary object
    note = Note.query.get(noteId)  # Get that Note's primary key
    if note:
        if note.user_id == current_user.id:  # If the user owns the note,
            db.session.delete(note)  # Then delete it
            db.session.commit()  # Commit the changes to the db
    return jsonify({})  # Return an empty response
