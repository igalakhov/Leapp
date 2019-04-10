from config import *
from leapp.models import db
from flask import Flask
from leapp.routes import thing

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

app.register_blueprint(thing)