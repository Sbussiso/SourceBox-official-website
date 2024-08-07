from flask import Blueprint, render_template, request, flash, redirect, url_for, abort, session
from flask_login import login_required, current_user
from werkzeug.utils import safe_join
from functools import wraps
import requests
from .. import db
import os
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

service = Blueprint('service', __name__, template_folder='templates')

API_URL = os.getenv('API_URL')  # Ensure this is set in your .env file

def record_user_history(action):
    token = session.get('access_token')  # Get token from session
    if token:
        headers = {'Authorization': f'Bearer {token}'}
        data = {'action': action}
        logger.info(f"Recording user history with headers: {headers} and data: {data}")
        response = requests.post(f"{API_URL}/user_history", json=data, headers=headers)
        if response.status_code != 201:
            logger.error(f"Failed to record user history: {response.text}")
            flash('Failed to record user history', 'error')

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = session.get('access_token')  # Ensure we are getting the token from session
        logger.info(f"Checking token: {token}")
        if not token:
            flash("Please log in to access this page.", "warning")
            return redirect(url_for('auth.login'))
        
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(f"{API_URL}/user_history", headers=headers)  # Validate token
        if response.status_code != 200:
            logger.error(f"Token validation failed: {response.text}")
            flash("Session expired or invalid. Please log in again.", "warning")
            return redirect(url_for('auth.login'))
        
        return f(*args, **kwargs)
    return decorated_function

@service.route('/service/wikidoc')
@token_required
def wikidoc():
    record_user_history("entered wikidoc")
    return redirect("https://sourcebox-wikidoc-d6286dbab352.herokuapp.com") # link to wikidoc stand alone app

@service.route('/service/codedoc')
@token_required
def codedoc():
    record_user_history("entered codedoc")
    return render_template('codedoc.html')

@service.route('/service/source-lightning')
@token_required
def source_lightning():
    record_user_history("entered source-lightning")
    return render_template('source_lightning.html')

@service.route('/service/pack-man')
@token_required
def pack_man():
    record_user_history("entered pack-man")
    return redirect("https://sourcebox-packman-418797343a6b.herokuapp.com") # link to packman stand alone app

@service.route('/service/source-mail')
@token_required
def source_mail():
    record_user_history("entered source-mail")
    return render_template('source_mail.html')
