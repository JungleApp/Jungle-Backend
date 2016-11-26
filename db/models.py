#     __             _
#  __|  |_ _ ___ ___| |___
# |  |  | | |   | . | | -_|
# |_____|___|_|_|_  |_|___|
#              |___|
#
# App-Models
# Last Revision: 11/26/16

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))
    join_date = db.Column(db.DateTime)
    last_login = db.Column(db.DateTime)
    name = db.Column(db.String(128))
    location = db.Column(db.String(128))
    points = db.Column(db.Integer, )
    num_posts = db.Column(db.Integer)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.email
