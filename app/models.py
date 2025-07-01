#!/usr/bin/env python3

from flask_login import UserMixin, AnonymousUserMixin
from app.extensions import db

class Anonymous(AnonymousUserMixin):
    id = 0
    name = 'Guest'
    username = 'Guest'
    email = ''
    password = ''
    role = None    

class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)
    created = db.Column(db.String, nullable=False)
