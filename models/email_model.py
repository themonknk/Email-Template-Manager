from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Email(db.Model):
    __tablename__ = 'emails'
    id = db.Column(db.Integer, primary_key=True)
    recipient = db.Column(db.String(150), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)
    scheduled_time = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(50), default='Scheduled')  # Possible values: Scheduled, Sent, Failed

    def __repr__(self):
        return f'<Email {self.subject}>'