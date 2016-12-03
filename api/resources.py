#     __             _
#  __|  |_ _ ___ ___| |___
# |  |  | | |   | . | | -_|
# |_____|___|_|_|_  |_|___|
#              |___|
#
# App-Resources
# Last Revision: 11/29/16

from flask_restful import Resource, abort, reqparse
from database.session import ssession
from database.models import User, Post, Media
import json
from flask_httpauth import HTTPBasicAuth
import hashlib


parser = reqparse.RequestParser()
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(email_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(email_or_token)
    if not user:
        user = ssession.query(User).filter_by(email=email_or_token).first()
        if not hasattr(user, 'password') or hashlib.sha224(password).hexdigest() not in user.password:
            return False
    g.user = user
    return True


class UserData(Resource):

    def get(self, user_id=None):
        #if not user_id:
            # Return a list of all the users
            #abort(400, error="GET request expects a user id parameter")

        res = ssession.query(User).filter_by(id=user_id).first()

        # There doesn't seem to be a sensible way to serialize this :(
        return {'id': res.id, 'email': res.email, 'password': res.password,
                'join_date': res.join_date.isoformat(),
                'last_login': res.last_login.isoformat(),
                'login_count': res.login_count, 'name': res.name,
                'location': res.location, 'points': res.points,
                'num_posts': res.num_posts}

class PostData(Resource):
    def get(self, post_id=None):
        return ssession.query(Post).first()

class MediaData(Resource):
    def get(self, media_id=None):
        return ''


