#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

sys.path.append(os.path.abspath('../'))
from config import DATABASE_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app)

from app import urls, views, models
