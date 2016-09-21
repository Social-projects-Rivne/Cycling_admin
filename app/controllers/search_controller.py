#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module add posibility to search users by admin.
"""
import sys, os
sys.path.append(os.path.abspath('..//..//'))
from app import app
from app import db
from app.models.User import User
import flask_whooshalchemy as wa

app.config['SQLALCHEMY_DATABASE_URI']='mysql://denny:isurrender@localhost/local_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['WHOOSH_BASE'] = 'whoosh'

def search_create_user(value):
    wa.whoosh_index(app, User)
    result = User.query.whoosh_search(value).first()
    return result

if __name__ == '__main__':
    print search_create_user("Hello@gmail.com")