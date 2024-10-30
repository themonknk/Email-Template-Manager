from flask import Blueprint, request, jsonify
from models.follow_up_model import FollowUpEmail, db
from api.email_utils import send_scheduled_email
from datetime import datetime, timedelta
from models.analytics_model import EmailAnalytics

follow_up_bp = Blueprint('follow_up', __name__)

@follow_up_bp.route('/create_follow_up', methods=['POST'])
def create_follow_up():
    data = request.json
    email_id = data.get('email_id')
    condition = data.get('condition')  # e.g., 'opened', 'clicked'
    follow_up_delay = data.get('delay')  # e.g., '2 days'
    follow_up_content = data.get('content')

    # Parse the follow-up delay into a datetime object
    delay_time = datetime.utcnow() + timedelta(days=int(follow_up_delay))

    new_follow_up = FollowUpEmail(
        email_id=email_id,
        condition=condition,
        follow_up_time=delay_time,
        follow_up_content=follow_up_content
    )

    db.session.add(new_follow_up)
    db.session.commit()

    return jsonify({'message': 'Follow-up email created successfully', 'follow_up_id': new_follow_up.id}), 201

def check_and_trigger_follow_up(email_id):
    analytics = EmailAnalytics.query.filter_by(email_id=email_id).first()
    follow_ups = FollowUpEmail.query.filter_by(email_id=email_id, status='Pending').all()

    for follow_up in follow_ups:
        if follow_up.condition == 'opened' and analytics.opens > 0:
            send_scheduled_email.apply_async(args=[follow_up.id], eta=follow_up.follow_up_time)
            follow_up.status = 'Sent'
            db.session.commit()
        elif follow_up.condition == 'clicked' and analytics.clicks > 0:
            send_scheduled_email.apply_async(args=[follow_up.id], eta=follow_up.follow_up_time)
            follow_up.status = 'Sent'
            db.session.commit()