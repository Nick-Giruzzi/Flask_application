#!/usr/bin/env python3

import subprocess, io
from flask import Blueprint, render_template_string, render_template, request, Response, current_app, send_file, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required

# Local Imports
from app.extensions import db, globals
from app.functions import *
from app.models import Anonymous, User

auth = Blueprint("auth",__name__) # add `, template_folder=f'templates', static_folder=f'static'` if url_prefix is enabled & blueprint unique templates and static folders are wanted

@auth.route("/auth", methods=["GET","POST"])
@login_required
def home():
    return render_template("auth.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))
