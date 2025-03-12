#!/usr/bin/env python3

import subprocess, os, logging
from flask_apscheduler import APScheduler
from datetime import timedelta, time

## Add entries below if you want variables to be able to be called, updated, and tracked throughout entire website

class Globals():
    def __init__(self):
        self.basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))