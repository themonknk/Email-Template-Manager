from flask_mail import Message
from flask import current_app
from models.email_model import Email, db

def send_scheduled_email(email_id):
    """
    Sends an email using Flask-Mail based on the email ID from the database.
    
    :param email_id: The ID of the email to be sent from the database.
    """
    with current_app.app_context():
        email = Email.query.get(email_id)
        if not email:
            print(f"Email with ID {email_id} not found.")
            return

        msg = Message(
            subject=email.subject,
            recipients=[email.recipient],
            body=email.body,
            sender='no-reply@yourdomain.com'
        )
        mail = current_app.extensions['mail']  # Use the mail instance from the app context
        mail.send(msg)
        print(f"Scheduled email with ID {email_id} sent successfully.")

def create_and_store_email(recipient, subject, body, schedule_time=None):
    """
    Creates a new email record in the database and stores it for future sending.
    
    :param recipient: The email address of the recipient.
    :param subject: The subject of the email.
    :param body: The body content of the email.
    :param schedule_time: Optional datetime when the email should be sent.
    :return: The created email object.
    """
    new_email = Email(
        recipient=recipient,
        subject=subject,
        body=body,
        scheduled_time=schedule_time
    )
    db.session.add(new_email)
    db.session.commit()
    print(f"Email with ID {new_email.id} created and stored successfully.")
    return new_email

def send_email_now(recipient, subject, body):
    """
    Sends an email immediately using Flask-Mail.
    
    :param recipient: The email address of the recipient.
    :param subject: The subject of the email.
    :param body: The body content of the email.
    """
    with current_app.app_context():
        msg = Message(
            subject=subject,
            recipients=[recipient],
            body=body,
            sender='no-reply@yourdomain.com'
        )
        mail = current_app.extensions['mail']  # Use the mail instance from the app context
        mail.send(msg)
        print(f"Email sent immediately to {recipient}.")