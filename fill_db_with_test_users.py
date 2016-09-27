#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app
from app import db
from app.models.user import User
from fixtures.fake_users import USERS
import random

emails = ['yahoo', 'gmail', 'zoho', 'outlook', 'aim']

def make_name(usr_dict):
    return '%s %s' % (usr_dict['name'], usr_dict['surname'])

def make_email(usr_dict):
    return '%s.%s@%s.com' % (usr_dict['name'], usr_dict['surname'], random.choice(emails))

db.create_all()

for line in USERS:
    u = User(full_name = make_name(line),
             email=make_email(line),
             password='1', is_active=True, role_id='0')
    db.session.add(u)
    db.session.commit()
    print '.',

db.session.remove()