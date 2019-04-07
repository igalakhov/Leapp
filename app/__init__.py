from config import *
from app.routes import app
from app.models import db

app.config['SECRET_KEY'] = 'secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

with app.test_request_context():
    db.init_app(app)
    db.create_all()

print(db)
print(db.metadata.tables.keys())