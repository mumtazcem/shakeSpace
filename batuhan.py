from flask import Blueprint, render_template
from datetime import datetime
from flask import current_app

batuhan = Blueprint('batuhan', __name__)

@batuhan.route('/announcements')

def announcements_page():
    now = datetime.now()
    day = now.strftime('%A')
    return render_template('announcements.html', day_name=day)
