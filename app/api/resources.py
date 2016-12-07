#     __             _
#  __|  |_ _ ___ ___| |___
# |  |  | | |   | . | | -_|
# |_____|___|_|_|_  |_|___|
#              |___|
#
# App-Resources
# Last Revision: 12/5/16

import hashlib
from flask import jsonify, Blueprint
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, reqparse, Api
from app.api.models import User, Post, Media, \
    user_schema, post_schema, media_schema
from app import db

#api = Api(app)
parser = reqparse.RequestParser()
auth = HTTPBasicAuth()

api_blueprint = Blueprint('apiblueprint', __name__)


@auth.verify_password
def verify_password(email_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(email_or_token)
    if not user:
        user = User.query.filter_by(email=email_or_token).first()
        if not hasattr(user, 'password') or hashlib.sha224(password).hexdigest() not in user.password:
            return False
    g.user = user
    return True


class UserData(Resource):

    def get(self, user_id=None):
        if user_id is None:
            # Return a list of all the users
            usr = User.query.all()
        else:
            usr = User.query.filter_by(id=user_id).first()

        res = user_schema.dump(usr)
        return jsonify(res.data), 201


class PostData(Resource):
    def get(self, post_id=None):
        if post_id is None:
            pst = Post.query.all()
        else:
            pst = Post.query.filter_by(id=post_id).first()

        res = post_schema.dump(pst)
        return jsonify(res.data), 201

class MediaData(Resource):
    def get(self, media_id=None):
        if media_id is None:
            md = Media.query.all()
        else:
            md = Media.query.filter_by(id=media_id).first()

        res = media_schema.dump(md)
        return jsonify(res.data), 201

@api_blueprint.route('/api/testuser')
def adduser_api():
    usr = User('jrbartola@gmail.com', 'pass123', 'Jesse Bartola', 'Amherst')
    usr2 = User('johnny@gmail.com', 'thisisabadpassword', 'Johnny Depp', 'Slamherst')
    usr3 = User('jimmyjones@bones.com', 'abcdefg', 'JimmyJones III')
    usrs = [usr, usr2, usr3]
    for u in usrs:
        tried = db.session.query(User).filter_by(email=u.email).first()
        if not tried:
            try:
                db.session.add(u)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return 'Rollback because of ' + str(e)
    return 'Success!'


@api_blueprint.route('/api/testpost')
def addpost_api():
    p1 = Post(1, '''Hello all! I have finally guaranteed a housing appointment at...''')
    p2 = Post(16, '''Today a very tragic event occurred-- one that will plague us for eternity''')
    p3 = User(1, '''Another post made by me myself and I''')
    ps = [p1, p2, p3]
    for p in ps:
        tried = db.session.query(Post).filter_by(id=p.id).first()
        if not tried:
            try:
                db.session.add(p)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return 'Rollback because of ' + str(e)
    return 'Success!'

@api_blueprint.route('/api/testmedia')
def addmedia_api():
    m1 = Media(1, 1, '/var/log/supervisor/test.txt')
    m2 = Media(2, 1, '/home/www/flaskapp/hi.jpeg')
    m3 = Media(3, 16, '/root/home/logging/profile.gif')
    marr = [m1, m2, m3]
    for m in marr:
        tried = db.session.query(Media).filter_by(id=m.id).first()
        if not tried:
            try:
                db.session.add(m)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return 'Rollback because of ' + str(e)
    return 'Success!'



