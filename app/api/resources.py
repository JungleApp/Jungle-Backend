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
        return jsonify(res.data)


class PostData(Resource):
    def get(self, post_id=None):
        return Post.query.first()

class MediaData(Resource):
    def get(self, media_id=None):
        return Media.query.first()

@api_blueprint.route('/api/test')
def testapi():
    usr = User('jrbartola@gmail.com', 'pass123', 'Jesse Bartola', 'Amherst')
    usr2 = User('johnny@gmail.com', 'thisisabadpassword', 'Johnny Depp', 'Slamherst')
    usr3 = User('jimmyjones@bones.com', 'abcdefg', 'JimmyJones III')
    usrs = [usr, usr2, usr3]
    for u in usrs:
        tried = db.session.query(User).filter_by(email=u.email).first()
        if not tried:
            try:
                db.session.add(usr)
                db.session.add(usr2)
                db.session.add(usr3)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return 'Rollback because of ' + str(e)
    return 'success!'



