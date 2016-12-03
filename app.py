#     __             _
#  __|  |_ _ ___ ___| |___
# |  |  | | |   | . | | -_|
# |_____|___|_|_|_  |_|___|
#              |___|
#
# App-Backend
# Last Revision: 12/2/16

# ip: 138.197.4.56

from flask import Flask, request, session, g, url_for, jsonify
from flask_restful import Api
from api.resources import *
from database.models import User, Post, Media
from database.session import ssession
from flask_marshmallow import Marshmallow

app = Flask(__name__)
api = Api(app)
ma = Marshmallow(app)

# Setup our error logging
if app.debug is not True:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('errors.log', maxBytes=1024 * 1024 * 100, backupCount=20)
    file_handler.setLevel(logging.ERROR)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)

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

@app.route('/')
def index():
    return '<h1>Jungle</h1>'

@app.route('/api')
def api_route():
    q = ssession.query(User).first()
    res = user_schema.dump(q)
    return jsonify(res.data)


@app.errorhandler(404)
def four_oh_four(url):
    return '''
    <h1 style="color:red;">
    Whoops! Looks like you've entered an invalid url.
    </h1>
    '''


# Add resources to our URI identifiers
api.add_resource(UserData, '/api/user/<int:user_id>', '/api/user')
api.add_resource(PostData, '/api/post/<int:post_id>', '/api/post')
api.add_resource(MediaData, '/api/media/<int:media_id>', '/api/media')

if __name__ == '__main__':
    app.run(debug=False)