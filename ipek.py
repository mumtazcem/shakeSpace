from flask import Blueprint, render_template

ipek = Blueprint('ipek', __name__)

@ipek.route('/events')

def events_page():
    return render_template('events.html')