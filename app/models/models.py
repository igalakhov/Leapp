from flask_sqlalchemy import SQLAlchemy
from config import *
from app import app
from passlib.hash import bcrypt

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


# models
class User(db.Model):

    # single fields
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(127), nullable=False)
    last = db.Column(db.String(127), nullable=False)
    username = db.Column(db.String(127), unique=True, nullable=False)
    email = db.Column(db.String(127), unique=True, nullable=False)
    password = db.Column(db.String(127), nullable=False)
    email_consent = db.Column(db.Boolean, nullable=False, default=False)

    # relationships

    def __init__(self, first: str, last: str, username: str, email: str, password: str, consent: bool):
        self.first = first
        self.last = last
        self.username = username
        self.email = email
        self.password = bcrypt.encrypt(password)
        self.consent = consent

    def validate_password(self, password):
        return bcrypt.verify(password, self.password)

    def __repr__(self):
        return '<User %r>' % self.username
