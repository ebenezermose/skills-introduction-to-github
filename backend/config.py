import os

class Config:
    # General Flask settings
    SECRET_KEY = os.urandom(24)  # Session management key
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking for performance

    # Database URI
    SQLALCHEMY_DATABASE_URI = 'sqlite:///project_alpha.db'  # SQLite (local database for development)

    # Flask-Login Settings (User session management)
    LOGIN_DISABLED = False