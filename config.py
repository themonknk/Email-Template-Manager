import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super_secret_key_for_development'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///users.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'filesystem'  # Stores session data on the file system