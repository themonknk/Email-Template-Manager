from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class FileMetadata(db.Model):
    __tablename__ = 'file_metadata'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200), nullable=False)
    uploaded_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    uploaded_by = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<FileMetadata {self.filename}>'