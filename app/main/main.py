
import subprocess, io, os, datetime
from flask import Blueprint, render_template_string, render_template, request, Response, current_app, send_file, make_response, flash, url_for, redirect
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS

# Local Imports
from app.extensions import db, globals
#from app.functions import 
from app.models import Anonymous, User

main = Blueprint("main",__name__)       # add `, template_folder=f'templates', static_folder=f'static'` if url_prefix is enabled & blueprint unique templates and static folders are wanted
#CORS(main)

@main.route("/", methods=["GET","POST"])
def home():
    #return render_template_string("Home Page")
    return render_template("index.html")

@main.route("/login", methods=["GET","POST"])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else: 
        username = request.form.get('username')
        password = request.form.get('password')
        remember = True 
        #print(f'Username::pwd -- {username}::{password}')
        user = User.query.filter_by(un=username).first()
        # check if the user actually exists
        if user == None:
            #flash('Login incorrect')
            resp = make_response(render_template('login.html'),401)
            return resp
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
        if not check_password_hash(user.pwd,password):
            #flash('Login incorrect')
            resp = make_response(render_template('login.html'),401)
            return resp
        # if the above check passes, then we know the user has the right credentials
        login_user(user, remember=remember)
        resp = redirect(url_for('auth.home'))
        return resp

@main.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html")
    else:
        data = request.form
        check_existing = User.query.filter_by(un=data['username']).first() is not None
        if check_existing:
            flash("That username already exists.")
            return redirect(url_for('main.signup'))
        if data['password'] != data['confirmPassword']:
            flash("Passwords did not match. Please try again.")
            return redirect(url_for('main.signup'))
        new_user = User(un=data['username'], fn=data['firstName'], ln=data['lastName'], pwd=generate_password_hash(data['password']), created=datetime.datetime.now().strftime('%d-%m-%Y, %H:%M'))
        try:
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            print(f"Exception creating user: {str(e)}")
            flash("Error occurred creating account. Please try again")
            return redirect(url_for('main.signup'))
        else:
            flash("Account created successfully!")
            return redirect(url_for('main.login'))