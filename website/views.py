#Views.py
#Author: John Botonakis
#With help from "Tech With Tim" on Youtube
#Desc:
from datetime import datetime

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
import json

from . import db
from .models import Note

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('Note')
        if len(note)<3:
            flash('Note must be at least 3 characters!', category='error')
        else:
            new_note = Note(data = note, user_id = current_user.id, date = datetime.now())
            db.session.add(new_note)
            db.session.commit()
            flash('Note successfully added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id: #If the user owns the note,
            db.session.delete(note) #Then delete it
            db.session.commit() #Commit the changes to the db
    return jsonify({}) #Return an empty response