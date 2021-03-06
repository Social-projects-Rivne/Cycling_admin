#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Docstring
"""
import random
from .app import db
from .app.models.user import User
from .fixtures.fake_users import USERS

EMAILS = ['yahoo', 'gmail', 'zoho', 'outlook', 'aim']

def make_name(usr_dict):
    """ Docstring """
    return '%s %s' % (usr_dict['name'], usr_dict['surname'])

def make_email(usr_dict):
    """ Docstring """
    return '%s.%s@%s.com' % (usr_dict['name'], usr_dict['surname'], random.choice(EMAILS))

db.create_all()

for line in USERS:
    u = User(full_name=make_name(line),
             email=make_email(line),
             password='1', is_active=True, role_id='0')
    db.session.add(u)
    db.session.commit()
    print '.',

db.session.remove()
