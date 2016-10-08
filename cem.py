'''
Created on Oct 8, 2016

@author: mumta
'''
from flask import Blueprint, render_template

from datetime import datetime
from flask import current_app

cem = Blueprint('cem', __name__)


@cem.route('/moderators')
def moderators_page():
    now = datetime.now()
    day = now.strftime('%A')
    return render_template('moderators.html', day_name=day)