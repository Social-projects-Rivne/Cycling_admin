#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

# Make the WSGI interface available at the top level so wfastcgi can get it
wsgi_app = app.wsgi_app
