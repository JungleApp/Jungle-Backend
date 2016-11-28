#     __             _
#  __|  |_ _ ___ ___| |___
# |  |  | | |   | . | | -_|
# |_____|___|_|_|_  |_|___|
#              |___|
#
# App-Models
# Last Revision: 11/28/16

from app import app
from flask_restful import Api, Resource

api = Api(app)

class UserData(Resource):
    def get(self, user_id):
        # TODO: Insert call to mySQL here
        return ''

class PostData(Resource):
    def get(self, post_id):
        # TODO: Insert call to mySQL here
        return ''

class MediaData(Resource):
    def get(self, media_id):
        # TODO: Insert call to mySQL here
        return ''

