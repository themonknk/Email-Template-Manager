from flask import Blueprint, request, jsonify
from models.ab_test_model import ABTest, db
from api.email_utils import send_scheduled_email
from datetime import datetime
from models.analytics_model import EmailAnalytics

ab_testing_bp = Blueprint('ab_testing', __name__)

@ab_testing_bp.route('/create_ab_test', methods=['POST'])
def create_ab_test():
    data = request.json
    email_id = data.get('email_id')
    variant_a = data.get('variant_a')
    variant_b = data.get('variant_b')
    test_duration = data.get('duration')  # Duration in days

    new_ab_test = ABTest(
        email_id=email_id,
        variant_a=variant_a,
        variant_b=variant_b,
        test_start_date=datetime.utcnow(),
        test_end_date=datetime.utcnow() + timedelta(days=int(test_duration))
    )

    db.session.add(new_ab_test)
    db.session.commit()

    return jsonify({'message': 'A/B test created successfully', 'ab_test_id': new_ab_test.id}), 201

def update_ab_test_results(email_id, variant):
    ab_test = ABTest.query.filter_by(email_id=email_id).first()
    analytics = EmailAnalytics.query.filter_by(email_id=email_id).first()

    if variant == 'A':
        ab_test.variant_a_opens += analytics.opens
        ab_test.variant_a_clicks += analytics.clicks
    elif variant == 'B':
        ab_test.variant_b_opens += analytics.opens
        ab_test.variant_b_clicks += analytics.clicks

    db.session.commit()