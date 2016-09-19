#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_whooshalchemy as wa

from app import app
from app.models.User import User

app.config['SQLALCHEMY_DATABASE_URI']='mysql://denny:isurrender@localhost/local_db'

wa.whoosh_index(app, User)
