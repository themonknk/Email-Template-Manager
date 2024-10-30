from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class FollowUpEmail(db.Model):
    __tablename__ = 'follow_up_emails'
    id = db.Column(db.Integer, primary_key=True)
    email_id = db.Column(db.Integer, db.ForeignKey('emails.id'), nullable=False)
    condition = db.Column(db.String(50), nullable=False)  # e.g., 'opened', 'clicked'
    follow_up_time = db.Column(db.DateTime, nullable=False)
    follow_up_content = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default='Pending')  # Possible values: Pending, Sent, Failed

    def __repr__(self):
        return f'<FollowUpEmail {self.email_id}>'