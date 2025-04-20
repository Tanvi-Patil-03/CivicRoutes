from flask import Flask
from routes import bp as routes_blueprint
from extensions import db  # ✅ now safely imported
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "supersecret")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

# Register the Blueprint
app.register_blueprint(routes_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
