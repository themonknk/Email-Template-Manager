from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.user_model import User
import re  # For email validation

login_bp = Blueprint('login', __name__, template_folder='../templates')

import re  # Make sure this import is at the top of the file

@login_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        identifier = request.form.get('identifier')  # This is the email or username
        password = request.form.get('password')

        # Debugging print to check input values
        print(f"Login attempt: identifier={identifier}, password={password}")

        # Check if the identifier is an email using regex or if it is a username
        if re.match(r"[^@]+@[^@]+\.[^@]+", identifier):
            user = User.query.filter_by(email=identifier).first()
            print(f"Checking email: {identifier}")
        else:
            user = User.query.filter_by(username=identifier).first()
            print(f"Checking username: {identifier}")

        # Debugging: Check if user was found in the database
        if user:
            print(f"User found: {user.username}")
        else:
            print("User not found")

        # Validate the password
        if user and user.check_password(password):
            # Set session variables after successful login
            session['user_id'] = user.id
            session['username'] = user.username
            session['logged_in'] = True  # Set logged_in to True
            print(f"Session after login: {session}")
            print("Password matched!")

            # Flash success message
            flash('Login successful! Welcome back.', 'success')
            print(f"Session before redirecting: {session}")
            print(f"Redirecting to dashboard...")

            # Redirect to the dashboard after successful login
            return redirect(url_for('dashboard.dashboard'))

        else:
            # Flash error message if login fails
            flash('Invalid credentials. Please check your email/username and password.', 'danger')
            print("Invalid login attempt")

        # Return to login page on failure
        return render_template('login.html')

    # Render login page on GET request
    print("Rendering login.html for GET request")
    return render_template('login.html')


@login_bp.route('/logout')
def logout():
    # Clear session on logout
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('logged_in', None)

    # Flash message after logging out
    flash('You have been logged out successfully.', 'info')

    # Redirect to the login page
    return redirect(url_for('login.login'))