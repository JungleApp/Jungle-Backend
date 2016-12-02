#     __             _
#  __|  |_ _ ___ ___| |___
# |  |  | | |   | . | | -_|
# |_____|___|_|_|_  |_|___|
#              |___|
#
# App-Backend
# Last Revision: 11/30/16

# ip: 138.197.4.56

from flask import Flask, request, session, g, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from api.resources import *
from database.models import User, Post, Media
from database.session import *

app = Flask(__name__)
api = Api(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:JungleDungle82@localhost/jungle'
# db = SQLAlchemy(app)

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
    return '''
    <h1>Jungle</h1>
    <br/>
    <h4>Wow. What an exciting application!</h4>
    '''

@app.route('/api')
def api_route():
    #from sqlalchemy import MetaData
    #Base.metadata.create_all(engine)
    #jesse = User('jrbartola@gmail.com', 'johnnydepp')
    #ssession.add(jesse)
    #ssession.commit()
    #return jsonify(json_list=ssession.query(User).order_by(User.id))
    return ssession.query(User).order_by(User.id).first()

@app.route('/errors')
def errors_route():
    errlog = open('errors.log', 'r+')
    fullresp = ''

    for line in errlog:
        fullresp += line + '\n'

    return fullresp

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