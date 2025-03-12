
import subprocess, io
from flask import Blueprint, render_template_string, render_template, request, Response, current_app, send_file, make_response, flash, url_for, redirect
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db
from app.functions import *
from app.models import Anonymous, User
import app.globals as globals


main = Blueprint("main",__name__)       # add `, template_folder=f'templates', static_folder=f'static'` if url_prefix is enabled & blueprint unique templates and static folders are wanted

@main.route("/", methods=["GET","POST"])
def home():
    return render_template_string("index.html")

@main.route("/login", methods=["GET","POST"])
@main.route("/login/", methods=["GET","POST"])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else: 
        username = request.form.get('username')
        password = request.form.get('password')
        remember = True 
        user = User.query.filter_by(username=username).first()
        # check if the user actually exists
        if user == None:
            flash('Login incorrect')
            resp = make_response(render_template('login.html'),401)
            return resp
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
        if user.password != password:
            flash('Login incorrect')
            resp = make_response(render_template('login.html'),401)
            return resp
        # if the above check passes, then we know the user has the right credentials
        login_user(user, remember=remember)
        resp = redirect(url_for('auth.home'))
        return resp
