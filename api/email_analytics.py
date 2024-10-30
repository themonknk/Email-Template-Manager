from flask import Blueprint, jsonify
from models.analytics_model import EmailAnalytics
from models.email_model import Email
from api.openai_helper.py import get_insights_from_data

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/get_advanced_email_analytics/<int:email_id>', methods=['GET'])
def get_advanced_email_analytics(email_id):
    analytics = EmailAnalytics.query.filter_by(email_id=email_id).first()
    if not analytics:
        return jsonify({'error': 'No analytics data found for this email'}), 404

    insights = get_insights_from_data({
        'opens': analytics.opens,
        'clicks': analytics.clicks,
        'bounces': analytics.bounces,
    })

    analytics_data = {
        'opens': analytics.opens,
        'clicks': analytics.clicks,
        'bounces': analytics.bounces,
        'open_rate': calculate_open_rate(analytics.opens, analytics.bounces),
        'click_rate': calculate_click_rate(analytics.clicks, analytics.opens),
        'insights': insights
    }
    return jsonify(analytics_data)

def calculate_open_rate(opens, bounces):
    return (opens / (opens + bounces)) * 100 if (opens + bounces) > 0 else 0

def calculate_click_rate(clicks, opens):
    return (clicks / opens) * 100 if opens > 0 else 0