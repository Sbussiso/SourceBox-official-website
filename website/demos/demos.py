from flask import Blueprint, render_template, request, flash, redirect, url_for, abort, send_from_directory
from flask_login import login_required, current_user
from werkzeug.utils import safe_join
from .. import db
from website.models import User, UserHistory



demos = Blueprint('demos', __name__, template_folder='templates')


def record_user_history(action):
     #record user history
    history = UserHistory(user_id=current_user.id, action=action)
    db.session.add(history)
    db.session.commit()



@demos.route('/demos/wikidoc')
@login_required
def wikidoc():
    record_user_history("entered wikidoc")

    return render_template('wikidoc.html')



@demos.route('/demos/codedoc')
@login_required
def codedoc():
    record_user_history("entered codedoc")
    
    return render_template('codedoc.html')