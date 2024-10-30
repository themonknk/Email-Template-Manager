from werkzeug.security import generate_password_hash, check_password_hash
from flask import session, redirect, url_for, render_template, request, flash, Blueprint
from models.user_model import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Dummy user store for demonstration (replace with a real database in production)
users = {"testuser": {"password": generate_password_hash("password123"), "id": 1}}

@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # Use 'identifier' to match the form field name
        identifier = request.form.get('identifier')
        password = request.form.get('password')

        print(f"Identifier: {identifier}, Password: {password}")  # Debugging print

        # Check if the identifier contains '@', treat it as an email, otherwise treat it as a username
        if '@' in identifier:
            user = User.query.filter_by(email=identifier).first()
        else:
            user = User.query.filter_by(username=identifier).first()

        # Ensure the user exists and password matches
        if user and user.check_password(password):
            login_user(user.id, user.username)  # Set session variables
            print(f"Login successful for {user.username}. Redirecting to dashboard...")
            return redirect(url_for('dashboard.dashboard'))

        flash('Invalid username/email or password.', 'danger')  # Error message for incorrect login
        return redirect(url_for('auth.login'))  # Stay on the login page for incorrect credentials

    print("Rendering login.html for GET request")
    return render_template('login.html')  # Render login page for GET request

@auth_bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(f"Username: {username}, Password: {password}")  # Debugging output

        # Check if user already exists
        if username in users:
            flash('Username already exists!', 'warning')
            return redirect(url_for('auth.register'))

        # Register the new user
        users[username] = {"password": hash_password(password), "id": len(users) + 1}
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('auth.login'))  # Redirect to login page after successful registration

    return render_template('register.html')  # Render register page for GET request

def hash_password(password):
    """Hash a plaintext password for secure storage."""
    return generate_password_hash(password)

def verify_password(stored_password, provided_password):
    """Verify a provided password against the stored hashed password."""
    return check_password_hash(stored_password, provided_password)

def login_user(user_id, username):
    """Logs in a user by setting session variables."""
    session['user_id'] = user_id
    session['username'] = username
    session['logged_in'] = True
    print(f"Session before redirecting: {session}")
    print(f"Session after login: {session}")  # Debug print
    flash(f"Welcome, {username}!", "success")  # Flash success message on login

def logout_user():
    """Logs out a user by clearing session variables."""
    session.clear()
    flash('You have been logged out successfully.', 'info')  # Flash logout message

def login_required(view_function):
    """Decorator to ensure routes are accessible only to logged-in users."""
    def wrapped_view(**kwargs):
        print(f"Session in login_required: {session}")  # Debug print

        # Check if the user is logged in by verifying 'user_id' in session
        if 'user_id' not in session:
            flash('Please log in first.', 'warning')
            return redirect(url_for('auth.login'))  # Redirect to login page

        # If logged in, proceed to the requested view
        return view_function(**kwargs)
    
    wrapped_view.__name__ = view_function.__name__
    return wrapped_view