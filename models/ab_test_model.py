from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class ABTest(db.Model):
    __tablename__ = 'ab_tests'
    id = db.Column(db.Integer, primary_key=True)
    email_id = db.Column(db.Integer, db.ForeignKey('emails.id'), nullable=False)
    variant_a = db.Column(db.Text, nullable=False)
    variant_b = db.Column(db.Text, nullable=False)
    test_start_date = db.Column(db.DateTime, nullable=False)
    test_end_date = db.Column(db.DateTime, nullable=False)
    variant_a_opens = db.Column(db.Integer, default=0)
    variant_b_opens = db.Column(db.Integer, default=0)
    variant_a_clicks = db.Column(db.Integer, default=0)
    variant_b_clicks = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<ABTest Email ID {self.email_id}>'