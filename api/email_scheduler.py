from celery import Celery
from datetime import datetime
from models.email_model import Email, db
from flask import current_app
from flask_mail import Mail
from flask import Blueprint, request, jsonify
from api.email_utils import create_and_store_email, send_scheduled_email  # Updated import statement

celery = Celery('email_scheduler', broker='redis://localhost:6379/0')
mail = Mail()

@celery.task
def schedule_send_email(email_id):
    """
    Celery task to send an email using the send_scheduled_email utility function.
    """
    send_scheduled_email(email_id)

schedule_bp = Blueprint('schedule', __name__)

@schedule_bp.route('/schedule_email', methods=['POST'])
def schedule_email():
    data = request.form
    recipient = data.get('recipient')
    subject = data.get('subject')
    body = data.get('body')
    schedule_time = datetime.strptime(data.get('schedule-time'), '%Y-%m-%dT%H:%M')

    new_email = Email(recipient=recipient, subject=subject, body=body, scheduled_time=schedule_time)
    db.session.add(new_email)
    db.session.commit()

    # Schedule the email using Celery
    schedule_send_email.apply_async(args=[new_email.id], eta=schedule_time)

    return jsonify({'message': 'Email scheduled successfully', 'email_id': new_email.id}), 201