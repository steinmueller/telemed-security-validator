from app import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Mission(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data_ecg = db.Column(db.String)
    # add more datatypes if necessary
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    local_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #remote_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    missions = db.relationship('Mission')