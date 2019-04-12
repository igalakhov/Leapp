from flask import Flask, redirect, url_for, flash
from config import *
from app.models import db
from app.models.models import User
from app.views.public.views import public_views

from flask_migrate import Migrate
from flask_session import Session
from flask_login import LoginManager, current_user

from functools import wraps
import pymysql

app = Flask(__name__)

# app constants
app.secret_key = SECRET_KEY
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SQLALCHEMY_DATABASE_URI'] = DIGITAL_OCEAN_DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

# database
pymysql.install_as_MySQLdb()  # lol
db.init_app(app)

with app.app_context():
    db.create_all()

# other stuff
migrate = Migrate(app, db)
session = Session(app)

# login stuff

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# blueprints
app.register_blueprint(public_views)

