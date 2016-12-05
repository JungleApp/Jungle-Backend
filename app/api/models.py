#     __             _
#  __|  |_ _ ___ ___| |___
# |  |  | | |   | . | | -_|
# |_____|___|_|_|_  |_|___|
#              |___|
#
# App-Models
# Last Revision: 11/29/16

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from app import db, ma
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

    email = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    login_count = db.Column(db.Integer, default=0)
    name = db.Column(db.String(128), default=None)
    location = db.Column(db.String(128), default=None)
    points = db.Column(db.Integer, default=0)
    num_posts = db.Column(db.Integer, default=0)

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
        user = User.query.get(data['id'])
        return user

# Classify Posts and Media as separate tables so we can join
class Post(Base):
    __tablename__ = 'Post'

    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    body = db.Column(db.BLOB, default="")

    def __init__(self, user_id, body):
        self.user_id = user_id
        self.body = body

    def __repr__(self):
        return '<Post %r>' % self.id

class Media(Base):
    __tablename__ = 'Media'

    post_id = db.Column(db.Integer, db.ForeignKey('Post.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    path = db.Column(db.String(128))

    def __init__(self, post_id, user_id, path):
        self.post_id = post_id
        self.user_id = user_id
        self.path = path

    def __repr__(self):
        return '<Media %r>' % self.path


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User


class PostSchema(ma.ModelSchema):
    class Meta:
        model = Post


class MediaSchema(ma.ModelSchema):
    class Meta:
        model = Media

user_schema = UserSchema()
post_schema = PostSchema()
media_schema = MediaSchema()
