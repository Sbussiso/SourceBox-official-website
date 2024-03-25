from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
import os
from os import path


#database
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "secret"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{DB_NAME}"
    db.init_app(app)

    #global template like base
    @app.context_processor
    def inject_user():
        return dict(current_user=current_user)



    from website.sourcebox.views import views
    from website.authentication.auth import auth
    from website.admin.admin import admin
    from website.demos.demos import demos

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/')
    app.register_blueprint(demos, url_prefix='/demos')
    

    from .models import User
    #from .models import PlatformUpdates
    create_database(app)

    Login_manager = LoginManager()
    Login_manager.login_view = 'auth.login'
    Login_manager.init_app(app)

    @Login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')