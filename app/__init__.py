#     __             _
#  __|  |_ _ ___ ___| |___
# |  |  | | |   | . | | -_|
# |_____|___|_|_|_  |_|___|
#              |___|
#
# App-Backend
# Last Revision: 12/3/16

# ip: 138.197.4.56

from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from flask_httpauth import HTTPBasicAuth
from flask.ext.sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
#from app.api.resources import api_blueprint
#from app.api.resources import UserData, PostData, MediaData

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)
api = Api(app)
ma = Marshmallow(app)

#app.register_blueprint(api_blueprint)

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

# Import a module / component using its blueprint handler variable (mod_auth)
#from app.mod_auth.controllers import mod_auth as auth_module

# Register blueprint(s)
#app.register_blueprint(auth_module)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
#db.create_all()

parser = reqparse.RequestParser()
auth = HTTPBasicAuth()

#api_blueprint = Blueprint('apiblueprint', __name__)


# api.add_resource(UserData, '/api/user/<int:user_id>', '/api/user')
# api.add_resource(PostData, '/api/post/<int:post_id>', '/api/post')
# api.add_resource(MediaData, '/api/media/<int:media_id>', '/api/media')
