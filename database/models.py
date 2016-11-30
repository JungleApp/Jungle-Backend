#     __             _
#  __|  |_ _ ___ ___| |___
# |  |  | | |   | . | | -_|
# |_____|___|_|_|_  |_|___|
#              |___|
#
# App-Models
# Last Revision: 11/29/16

from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, BLOB, \
    DateTime, ForeignKey

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    email = Column(String(64), unique=True)
    password = Column(String(255))
    join_date = Column(DateTime)
    last_login = Column(DateTime)
    login_count = Column(Integer, default=0)
    name = Column(String(128), default=None)
    location = Column(String(128), default=None)
    points = Column(Integer, default=0)
    num_posts = Column(Integer, default=0)

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.join_date = datetime.utcnow()
        self.last_login = datetime.utcnow()

    def __repr__(self):
        return '<User %r>' % self.email

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