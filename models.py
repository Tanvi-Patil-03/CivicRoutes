from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

# User model class
class User(UserMixin, db.Model):
    # Create the table 'user' with the following columns:
    id = db.Column(db.Integer, primary_key=True)  # Auto-incrementing user ID
    email = db.Column(db.String(120), unique=True, nullable=False)  # User's email
    username = db.Column(db.String(50), nullable=False)  # User's username
    password = db.Column(db.String(200), nullable=False)  # User's hashed password

    def __repr__(self):
        return f"<User {self.username}>"
