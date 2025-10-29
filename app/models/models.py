from app.extensions import db  # Assuming db is initialized with SQLAlchemy
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    bio = db.Column(db.String(500))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    # Coordinates for location-based matching
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    
    # Relationships
    # A User can have many Matches (as user1 or user2)
    matches_as_user1 = db.relationship('Match', foreign_keys='Match.user1_id', backref='user1', lazy='dynamic')
    matches_as_user2 = db.relationship('Match', foreign_keys='Match.user2_id', backref='user2', lazy='dynamic')
    # A User can send many Messages
    messages_sent = db.relationship('Message', foreign_keys='Message.sender_id', backref='sender', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'

class Match(db.Model):
    __tablename__ = 'matches'
    
    id = db.Column(db.Integer, primary_key=True)
    
    # Foreign Keys linking to the User model
    user1_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user2_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Status can be 'pending_u1_u2', 'pending_u2_u1', 'matched', 'rejected'
    status = db.Column(db.String(20), default='pending_u1_u2', nullable=False)
    
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    # Relationship: A Match can have many Messages
    conversation = db.relationship('Message', backref='match', lazy='dynamic')

    def __repr__(self):
        return f'<Match {self.user1_id} vs {self.user2_id}, Status: {self.status}>'

class Message(db.Model):
    __tablename__ = 'messages'
    
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(1000), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    # Foreign Keys
    match_id = db.Column(db.Integer, db.ForeignKey('matches.id'), nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<Message {self.id} from {self.sender_id}>'