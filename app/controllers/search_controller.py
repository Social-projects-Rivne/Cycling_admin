#!/usr/bin/env python
# -*- coding: utf-8 -*-
import flask_whooshalchemy as wa

import app

from app.models.User import User

app.app.config['SQLALCHEMY_DATABASE_URI']='mysql://denny:isurrender@localhost/local_db'

wa.whoosh_index(app, User)
