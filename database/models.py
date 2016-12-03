#     __             _
#  __|  |_ _ ___ ___| |___
# |  |  | | |   | . | | -_|
# |_____|___|_|_|_  |_|___|
#              |___|
#
# App-Models
# Last Revision: 11/29/16

from datetime import datetime
from sqlalchemy import Column, Integer, String, BLOB, \
    DateTime, ForeignKey
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from flask_marshmallow import Marshmallow
from app import db
from config import *

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(64), unique=True)
    password = Column(String(255))
    login_count = Column(Integer, default=0)
    name = Column(String(128), default=None)
    location = Column(String(128), default=None)
    points = Column(Integer, default=0)
    num_posts = Column(Integer, default=0)

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.email

    def generate_auth_token(self, expiration=600):
        s = Serializer(CSRF_SESSION_KEY, expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(CSRF_SESSION_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        ### Check this...
        user = User.query.get(data['n_id'])
        return user

# Classify Posts and Media as separate tables so we can join
class Post(Base):
    __tablename__ = 'Post'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    body = Column(BLOB, default="")
    date_posted = Column(DateTime)
    last_updated = Column(DateTime)

    def __init__(self, user_id, body):
        self.user_id = user_id
        self.body = body
        self.date_posted = datetime.utcnow()
        self.last_updated = datetime.utcnow()

    def __repr__(self):
        return '<Post %r>' % self.id

class Media(Base):
    __tablename__ = 'Media'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('Post.id'))
    user_id = Column(Integer, ForeignKey('User.id'))
    path = Column(String(128))

    def __init__(self, post_id, user_id, path):
        self.post_id = post_id
        self.user_id = user_id
        self.path = path

    def __repr__(self):
        return '<Media %r>' % self.path










from app import db



# Define a User model
class User(Base):

    __tablename__ = 'auth_user'

    # User Name
    name    = db.Column(db.String(128),  nullable=False)

    # Identification Data: email & password
    email    = db.Column(db.String(128),  nullable=False,
                                            unique=True)
    password = db.Column(db.String(192),  nullable=False)

    # Authorisation Data: role & status
    role     = db.Column(db.SmallInteger, nullable=False)
    status   = db.Column(db.SmallInteger, nullable=False)

    # New instance instantiation procedure
    def __init__(self, name, email, password):

        self.name     = name
        self.email    = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)