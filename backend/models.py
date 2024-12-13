from project_alpha.app import db
from flask_login import UserMixin

# User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    links = db.relationship('Link', backref='owner', lazy=True)  # One-to-many relationship with Link

    def __repr__(self):
        return f'<User {self.username}>'

# Link Model
class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    category = db.Column(db.String(50), nullable=False)
    network = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign Key to User model

    def __repr__(self):
        return f'<Link {self.title} by {self.owner.username}>'