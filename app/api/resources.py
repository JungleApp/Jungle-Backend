#     __             _
#  __|  |_ _ ___ ___| |___
# |  |  | | |   | . | | -_|
# |_____|___|_|_|_  |_|___|
#              |___|
#
# App-Resources
# Last Revision: 12/7/16

import hashlib
from flask import jsonify, Blueprint, g, request
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, reqparse
from app.api.models import User, Post, Media, \
    user_schema, post_schema, media_schema
from app import db


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
    decorators = [auth.login_required]

    def get(self, user_id=None):
        if user_id is None:
            # Return a list of all the users
            usr = User.query.all()
        else:
            usr = User.query.filter_by(id=user_id).first()

        # If no data matches our query send a 404
        if not usr:
            return jsonify({'response': None, 'status': 404})

        res = user_schema.dump(usr)
        return jsonify({'response': res.data, 'status': 200})

    def post(self):
        json_args = request.get_json()
        if not json_args:
            return jsonify({'response': 'Missing POST request arguments for User',
                            'status': 400})
        data, errors = user_schema.load(json_args)
        if errors:
            return jsonify({'response': 'Bad JSON arguments', 'status': 422})
        if 'email' not in data:
            return jsonify({'response': 'Missing \'email\' argument in POST request',
                            'status': 422})
        elif 'password' not in data:
            return jsonify({'response': 'Missing \'password\' argument in POST request',
                            'status': 422})
        email, password, name, location = data['email'], data['password'], None, None

        # Check if we have a name or location
        if 'name' in data:
            name = data['name']
        if 'location' in data:
            location = data['location']

        # Now we check for a duplicate user-- Must be unique email!
        dup = User.query.filter_by(email=email).first()
        if not dup:
            new_user = User(email, hashlib.sha224(password).hexdigest(), name, location)
            try:
                db.session.add(new_user)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return jsonify({'response': str(e), 'status': 422})

            # If we pass all the checks we're golden!
            new_user = user_schema.dump(new_user)
            return jsonify({'response': new_user.data, 'status': 200})
        else:
            return jsonify({'response': 'Duplicate User for email \'' + email + '\''})




class PostData(Resource):
    decorators = [auth.login_required]

    def get(self, post_id=None):
        if post_id is None:
            pst = Post.query.all()
        else:
            pst = Post.query.filter_by(id=post_id).first()

        # If no data matches our query send a 404
        if not pst:
            return jsonify({'response': None, 'status': 404})

        res = post_schema.dump(pst)
        return jsonify({'response': res.data, 'status': 200})

class MediaData(Resource):
    decorators = [auth.login_required]

    def get(self, media_id=None):
        if media_id is None:
            md = Media.query.all()
        else:
            md = Media.query.filter_by(id=media_id).first()

        # If no data matches our query send a 404
        if not md:
            return jsonify({'response': None, 'status': 404})

        res = media_schema.dump(md)
        return jsonify({'response': res.data, 'status': 200})

@api_blueprint.route('/api/testuser')
def adduser_api():
    usr = User('jrbartola@gmail.com', hashlib.sha224('pass123').hexdigest(), 'Jesse Bartola', 'Amherst')
    usr2 = User('johnny@gmail.com', hashlib.sha224('thisisabadpassword').hexdigest(), 'Johnny Depp', 'Slamherst')
    usr3 = User('jimmyjones@bones.com', hashlib.sha224('abcdefg').hexdigest(), 'JimmyJones III')
    usrs = [usr, usr2, usr3]
    for u in usrs:
        tried = db.session.query(User).filter_by(email=u.email).first()
        if not tried:
            try:
                db.session.add(u)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return 'Rollback because of ' + str(e)
    return 'Success!'


@api_blueprint.route('/api/testpost')
def addpost_api():
    p1 = Post(19, '''Hello all! I have finally guaranteed a housing appointment at...''')
    p2 = Post(19, '''Today a very tragic event occurred-- one that will plague us for eternity''')
    p3 = Post(21, '''Another post made by me myself and I''')
    ps = [p1, p2, p3]
    for p in ps:
        tried = db.session.query(Post).filter_by(id=p.id).first()
        if not tried:
            try:
                db.session.add(p)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return 'Rollback because of ' + str(e)
    return 'Success!'

@api_blueprint.route('/api/testmedia')
def addmedia_api():
    m1 = Media(4, 20, '/var/log/supervisor/test.txt')
    m2 = Media(5, 20, '/home/www/flaskapp/hi.jpeg')
    m3 = Media(6, 19, '/root/home/logging/profile.gif')
    marr = [m1, m2, m3]
    for m in marr:
        tried = db.session.query(Media).filter_by(id=m.id).first()
        if not tried:
            try:
                db.session.add(m)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return 'Rollback because of ' + str(e)
    return 'Success!'



