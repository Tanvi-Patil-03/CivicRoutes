from main import app
from models import User
from extensions import db

with app.app_context():
    db.create_all()
    print("✅ Database created successfully!")
