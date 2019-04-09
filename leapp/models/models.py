from flask_sqlalchemy import SQLAlchemy
from config import *
# from leapp.routes import app
from passlib.hash import bcrypt
from flask import Flask

# app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy()


# models
class User(db.Model):

    # single fields
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(127), nullable=False)
    last = db.Column(db.String(127), nullable=False)
    email = db.Column(db.String(127), unique=True, nullable=False)
    password = db.Column(db.String(127), nullable=False)
    email_consent = db.Column(db.Boolean, nullable=False, default=False)

    # basic init
    def __init__(self, first: str, last: str, email: str, password: str, consent: bool):
        self.first = first
        self.last = last
        self.email = email
        self.password = bcrypt.encrypt(password)
        self.consent = consent

    def validate_password(self, password):
        return bcrypt.verify(password, self.password)

    def __repr__(self):
        return '<User %r>' % self.email
