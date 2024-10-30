from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.user_model import User, db

register_bp = Blueprint('register', __name__, template_folder='../templates')

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Debugging prints to check input values
        print(f"Attempting to register: username={username}, email={email}")

        # Check if passwords match
        if password != confirm_password:
            flash('Passwords do not match. Please try again.', 'danger')
            return render_template('register.html')

        # Check if the email is already registered
        if User.query.filter_by(email=email).first():
            flash('Email already registered. Use a different email.', 'warning')
            print(f"Registration failed: {email} is already registered.")  # Debug print
            return redirect(url_for('register.register'))

        # Create a new user and add to the database
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        try:
            db.session.add(new_user)
            db.session.commit()
            print(f"User {username} registered successfully.")  # Debug print
        except Exception as e:
            db.session.rollback()  # Rollback if there's any error
            flash(f"Error occurred during registration: {str(e)}", 'danger')
            print(f"Error during registration: {str(e)}")  # Debug print
            return render_template('register.html')

        # Successful registration
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login.login'))

    return render_template('register.html')  # Render the register form for GET request