from config import *
from app.models import db
from flask import Flask
from app.routes import thing
from flask_migrate import Migrate
from flask_session import Session

app = Flask(__name__)

app.secret_key = SECRET_KEY
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

migrate = Migrate(app, db)
session = Session(app)


app.register_blueprint(thing)
