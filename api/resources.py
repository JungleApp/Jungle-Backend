#     __             _
#  __|  |_ _ ___ ___| |___
# |  |  | | |   | . | | -_|
# |_____|___|_|_|_  |_|___|
#              |___|
#
# App-Resources
# Last Revision: 11/29/16

from flask_restful import Resource
from database.session import ssession
from database.models import User, Post, Media
import json
import datetime, decimal


def alchemyencoder(obj):
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
        return float(obj)

class UserData(Resource):
    def get(self, user_id=None):
        # TODO: Insert call to mySQL here
        res = ssession.query(User).first()
        #return ssession.query(User).first()
        #return json.dumps([dict(r) for r in res], default=alchemyencoder)
        return {'id': res.id, 'email': res.email, 'password': res.password,
                'join_date': res.join_date.isoformat(),
                'last_login': res.last_login.isoformat(),
                'login_count': res.login_count, 'name': res.name,
                'location': res.location, 'points': res.points,
                'num_posts': res.num_posts}

class PostData(Resource):
    def get(self, post_id=None):
        # TODO: Insert call to mySQL here
        return ssession.query(Post).first()

class MediaData(Resource):
    def get(self, media_id=None):
        # TODO: Insert call to mySQL here
        return ''


