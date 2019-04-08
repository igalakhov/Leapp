from config import *
from app.routes import app
from app.models import db

app.config['SECRET_KEY'] = SECRET_KEY
