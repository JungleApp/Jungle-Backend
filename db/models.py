#     __             _
#  __|  |_ _ ___ ___| |___
# |  |  | | |   | . | | -_|
# |_____|___|_|_|_  |_|___|
#              |___|
#
# App-Models
# Last Revision: 11/26/16

from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))
    join_date = db.Column(db.DateTime)
    last_login = db.Column(db.DateTime)
    login_count = db.Column(db.Integer, default=0)
    name = db.Column(db.String(128), default=None)
    location = db.Column(db.String(128), default=None)
    points = db.Column(db.Integer, default=0)
    num_posts = db.Column(db.Integer, default=0)

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.join_date = datetime.utcnow()
        self.last_login = datetime.utcnow()

    def __repr__(self):
        return '<User %r>' % self.email

# Classify Posts and Media as separate tables so we can join
class Post(db.Model):
    __tablename__ = 'Post'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    body = db.Column(db.BLOB, default="")
    date_posted = db.Column(db.DateTime)
    last_updated = db.Column(db.DateTime)

    def __init__(self, user_id, body):
        self.user_id = user_id
        self.body = body
        self.date_posted = datetime.utcnow()
        self.last_updated = datetime.utcnow()

    def __repr__(self):
        return '<Post %r>' % self.id