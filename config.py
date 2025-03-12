#!/usr/bin/python3

import os, sys
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'NOT_A_TOKEN'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_APP = 'app.py'
    STATIC_FOLDER = f"{basedir}/app/static/"
    TEMPLATES_FOLDER = f"{basedir}/app/templates/"