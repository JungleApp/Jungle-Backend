#     __             _
#  __|  |_ _ ___ ___| |___
# |  |  | | |   | . | | -_|
# |_____|___|_|_|_  |_|___|
#              |___|
#
# App-Backend
# Last Revision: 12/5/16

# ip: 138.197.4.56

from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
#from app.api.resources import UserData, PostData, MediaData

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)
api_ = Api(app)
ma = Marshmallow(app)


from app.api.resources import api_blueprint as blue

app.register_blueprint(blue)

# Setup our error logging
if app.debug is not True:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('errors.log', maxBytes=1024 * 1024 * 100, backupCount=20)
    file_handler.setLevel(logging.ERROR)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)


@app.route('/')
def index():
    return '<h1>Jungle</h1>'


@app.errorhandler(404)
def four_oh_four(url):
    return '''
    <h1 style="color:red;">
    Whoops! Looks like you've entered an invalid url.
    </h1>
    '''

# Build the database:
db.create_all()

# Register blueprint(s)
from app.api.resources import UserData, PostData, MediaData

api_.add_resource(UserData, '/api/user/<int:user_id>', '/api/user')
api_.add_resource(PostData, '/api/post/<int:post_id>', '/api/post')
api_.add_resource(MediaData, '/api/media/<int:media_id>', '/api/media')
