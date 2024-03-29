from my_server import db, loginmanager
from datetime import datetime
from flask_login import UserMixin

@loginmanager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return f'USER:{self.username}, EMAIL:{self.username}'


class Mail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    sender = db.Column(db.String(120), nullable=False)
    to = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(88), nullable=False)
    body = db.Column(db.String(2000), nullable=False)
    
    @property
    def serialize(self):
        return {
            'sender': self.sender,
            'to': self.to,
            'subject': self.subject,
            'body': self.body
        }

    def __repr__(self):
        return f'{self.sender}, {self.subject}, '