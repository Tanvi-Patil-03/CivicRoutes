from flask import Blueprint, request, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from models import User  # Assuming you have a User model defined in models.py
from extensions import db  # Assuming you're using SQLAlchemy

# Create a single Blueprint for authentication and general routes
bp = Blueprint('routes', __name__)

# Route for Home (index page)
@bp.route('/')
def home():
    return render_template('index.html')  # Make sure 'index.html' exists in templates folder

# Route for Registration
@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered!', 'error')
            return redirect(url_for('routes.register'))

        # Hash password
        hashed_password = generate_password_hash(password, method='sha256')

        # Create new user
        new_user = User(email=email, username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful!', 'success')
        return redirect(url_for('routes.login'))  # Redirect to login after registration

    return render_template('register.html')

# Route for Login
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if user exists
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            flash('Login failed. Check your email and/or password', 'error')
            return redirect(url_for('routes.login'))

        login_user(user)
        flash('Login successful!', 'success')
        return redirect(url_for('routes.home'))  # Redirect to home page after login

    return render_template('login.html')

# Route for Chatbot
@bp.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")  # Assuming you have a chatbot page

@bp.route('/report')
def report():
    return render_template('report.html')  # Make sure this file exists in /templates


# Route for Logout
@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('routes.login'))  # Redirect to login page after logout
