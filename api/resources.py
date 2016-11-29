#     __             _
#  __|  |_ _ ___ ___| |___
# |  |  | | |   | . | | -_|
# |_____|___|_|_|_  |_|___|
#              |___|
#
# App-Models
# Last Revision: 11/28/16

from flask_restful import Resource


class UserData(Resource):
    def get(self, user_id=None):
        # TODO: Insert call to mySQL here
        return ''

class PostData(Resource):
    def get(self, post_id=None):
        # TODO: Insert call to mySQL here
        return ''

class MediaData(Resource):
    def get(self, media_id=None):
        # TODO: Insert call to mySQL here
        return ''


