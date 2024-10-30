from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class EmailAnalytics(db.Model):
    __tablename__ = 'email_analytics'
    id = db.Column(db.Integer, primary_key=True)
    email_id = db.Column(db.Integer, db.ForeignKey('email_model.id'), nullable=False)
    opens = db.Column(db.Integer, default=0)
    clicks = db.Column(db.Integer, default=0)
    bounces = db.Column(db.Integer, default=0)
    last_updated = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<EmailAnalytics for Email ID {self.email_id}>'