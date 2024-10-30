from flask import Flask, render_template, redirect, url_for, session
from flask_session import Session
from flask_mail import Mail
from config import Config
from models.user_model import db
from auth.auth_utils import login_required
from auth.auth_utils import auth_bp  # Import auth blueprint
from auth.login import login_bp  # Import login blueprint
from auth.register import register_bp  # Import register blueprint
from api.email_scheduler import schedule_bp
from api.file_manager import file_manager_bp
from api.follow_up_manager import follow_up_bp
from api.ab_testing_manager import ab_testing_bp
from api.dashboard_manager import dashboard_bp
from api.insights_manager import insights_bp
from api.report_manager import report_bp
from api.feedback_manager import feedback_bp
from api.ai_model_manager import ai_model_bp
from api.collaborative_manager import collaborative_bp, socketio
from api.template_editor_manager import template_editor_bp
from api.user_behavior_manager import user_behavior_bp
from api.sync_manager import sync_bp
from api.third_party_integration import third_party_bp
from auth.security_manager import hash_password, verify_password
from auth.auth_utils import auth_bp, login_required  # Import auth utilities and blueprint

# Initialize the Flask application
app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'your_secret_key_here'  # Required for flash messages

# Ensure Flask debugging tool is configured properly  
# Configure session to use the filesystem (or another option like Redis)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Initialize Flask-Mail with the app configuration
mail = Mail(app)

# Initialize the database with the Flask app
db.init_app(app)

# Initialize SocketIO with the Flask app
socketio.init_app(app)

# Register Blueprints for modular routing
app.register_blueprint(auth_bp, url_prefix='/auth')  # Auth blueprint

# Register blueprints for login and register
app.register_blueprint(login_bp, url_prefix='/auth')  # Register the login blueprint
app.register_blueprint(register_bp, url_prefix='/auth')  # Register the register blueprint

# Register blueprints with unique names and avoid duplicates
app.register_blueprint(dashboard_bp, url_prefix='/dashboard')  # Dashboard blueprint

# Other blueprints for API, templates, and other features
app.register_blueprint(schedule_bp, url_prefix='/api')
app.register_blueprint(file_manager_bp, url_prefix='/api')
app.register_blueprint(follow_up_bp, url_prefix='/api')
app.register_blueprint(ab_testing_bp, url_prefix='/api')
app.register_blueprint(insights_bp, url_prefix='/api')
app.register_blueprint(report_bp, url_prefix='/api')
app.register_blueprint(feedback_bp, url_prefix='/api')
app.register_blueprint(ai_model_bp, url_prefix='/api')
app.register_blueprint(collaborative_bp, url_prefix='/api')
app.register_blueprint(user_behavior_bp, url_prefix='/api')
app.register_blueprint(sync_bp, url_prefix='/api')
app.register_blueprint(third_party_bp, url_prefix='/api')
app.register_blueprint(template_editor_bp, url_prefix='/templates')

# Home route to display the base template
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test-login')
def test_login():
    # Simulate a logged-in user by setting session variables directly
    session['user_id'] = 1  # Use an ID of a test user
    session['username'] = 'testuser'
    session['logged_in'] = True
    return redirect(url_for('dashboard'))  # Redirect to the dashboard route

# Dashboard route - requires user to be logged in
@app.route('/dashboard')
@login_required
def dashboard():
    print("Accessing dashboard...")  # Debug print
    username = session.get('username')
    return render_template('dashboard.html', username=username)

# Settings route - requires user to be logged in
@app.route('/settings')
@login_required
def settings():
    return render_template('settings.html')

# Analytics route - requires user to be logged in
@app.route('/analytics')
@login_required
def analytics():
    return render_template('analytics.html')

# Profile route
@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

# Generate Report route
@app.route('/generate_report')
@login_required
def generate_report():
    return render_template('report_generation.html')

# Email Campaigns Routes
@app.route('/email_campaigns')
@login_required
def email_campaigns():
    return render_template('select_template.html')

@app.route('/create_email')
@login_required
def create_email():
    return render_template('create_template.html')

@app.route('/email_history')
@login_required
def email_history():
    return render_template('email_preview.html')

@app.route('/ab_testing')
@login_required
def ab_testing():
    return render_template('ab_testing.html')

@app.route('/scheduled_emails')
@login_required
def scheduled_emails():
    return render_template('schedule_email.html')

# Error handling for 404 Not Found
@app.errorhandler(404)
def page_not_found(e):
    print(f"404 Error: {e}")
    return render_template('error.html', error="404 - Page Not Found"), 404

# Error handling for 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    print(f"500 Error: {e}")
    return render_template('error.html', error="500 - Internal Server Error"), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(debug=True)