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

class UserData(Resource):
    def get(self, user_id=None):
        # TODO: Insert call to mySQL here

        return ssession.query(User).first()

class PostData(Resource):
    def get(self, post_id=None):
        # TODO: Insert call to mySQL here
        return ''

class MediaData(Resource):
    def get(self, media_id=None):
        # TODO: Insert call to mySQL here
        return ''


