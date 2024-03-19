from flask import Blueprint, render_template, request, flash, redirect, url_for, abort, send_from_directory
from flask_login import login_required
from werkzeug.utils import safe_join
import os

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/landing')
def landing():
    return render_template('landing.html')

@views.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@views.route('/updates')
def updates():
    return render_template('updates.html')

@views.route('/demos')
@login_required
def demos():
    return render_template('demos.html')

@views.route('/docs')
def documentation():
    return render_template('docs.html')

@views.route('/user_settings')
@login_required
def user_settings():
    return render_template('user_settings.html')


@views.route('/premium_info')
def premeum_info():
    return render_template('premium_info.html')

#download boilerplate landing.html example
DOWNLOAD_DIRECTORY = os.path.join(os.getcwd(), 'boilerbox')
@views.route('/download_plate/<filename>')
def download_plate(filename):
    # Prevent directory traversal vulnerability
    safe_path = safe_join(DOWNLOAD_DIRECTORY, filename)

    # Check if the file exists
    if not os.path.isfile(safe_path):
        abort(404)

    # Serve the file for download
    return send_from_directory(DOWNLOAD_DIRECTORY, filename, as_attachment=True)


@views.route('/sent_analysis')
def sent_analysis():
    pass

