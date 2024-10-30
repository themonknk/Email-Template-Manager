from flask import Blueprint, jsonify, render_template
from models.analytics_model import EmailAnalytics
from models.ab_test_model import ABTest
from models.email_model import Email

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard_bp.route('/')
def dashboard():
    return render_template('dashboard.html')

@dashboard_bp.route('/get_email_performance', methods=['GET'])
def get_email_performance():
    # Fetch performance data and summarize it
    data = {
        'labels': ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
        'openRates': [25, 40, 55, 70],
        'clickRates': [10, 20, 30, 45]
    }
    return jsonify(data)

@dashboard_bp.route('/get_ab_test_summary', methods=['GET'])
def get_ab_test_summary():
    # Fetch A/B test summary data
    summary = {
        'variantA': {'openRate': 45},
        'variantB': {'openRate': 60}
    }
    return jsonify(summary)

@dashboard_bp.route('/get_scheduled_emails', methods=['GET'])
def get_scheduled_emails():
    # Mock data for scheduled emails
    emails = [
        {'subject': 'New Year Promo', 'recipient': 'user@example.com', 'scheduledDate': '2024-12-31T09:00:00', 'status': 'Scheduled'},
        {'subject': 'Holiday Sale', 'recipient': 'customer@example.com', 'scheduledDate': '2024-12-20T12:00:00', 'status': 'Sent'}
    ]
    return jsonify(emails)

@dashboard_bp.route('/get_recent_activity', methods=['GET'])
def get_recent_activity():
    # Mock data for recent activity
    activity = [
        {'description': 'Created a new A/B test for Holiday Sale campaign', 'timestamp': '2024-10-01T14:00:00'},
        {'description': 'Scheduled follow-up emails for New Year Promo', 'timestamp': '2024-10-03T10:30:00'}
    ]
    return jsonify(activity)

@dashboard_bp.route('/get_notifications', methods=['GET'])
def get_notifications():
    notifications = [
        {'message': 'A/B Test for Campaign X reached a significant milestone.', 'timestamp': '2024-10-05T14:00:00'},
        {'message': 'Follow-up email sent successfully.', 'timestamp': '2024-10-06T10:00:00'}
    ]
    return jsonify(notifications)