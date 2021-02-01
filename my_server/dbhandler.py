from my_server import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return f'USER:{self.username}, EMAIL:{self.username}'

class Mail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    to = db.Column(db.String(120), unique=True, nullable=False)
    fromt = db.Column(db.String(120), unique=True, nullable=False)
    subject = db.Column(db.String(88), unique=True, nullable=False)
    text = db.Column(db.String(2000), nullable=False)
  