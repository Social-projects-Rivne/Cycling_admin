#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Testing ability get a role from a User instance.
"""

import unittest

import sys, os
sys.path.append(os.path.abspath('../'))
basedir = os.path.abspath(os.path.dirname(__file__))

import random

from app import app
from app import db
from app.models.user import User

trail1 = random.randint(100,1000)
trail2 = random.randint(100,1000)

class TestROle(unittest.TestCase):

    """Test case for getting a role from a user"""

    def setUp(self):
        """Init database."""
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(basedir, 'test.db')
        db.create_all()

    def test_regular_user(self):
        u = User(full_name='test user', email='test%s@gmail.com' % trail1,
                         password='1', is_active=True, role_id=0)
        db.session.add(u)
        db.session.commit()
        assert u.role() == 'user'

    def test_admin(self):
        u = User(full_name='test user', email='test%s@gmail.com' % trail2,
                         password='1', is_active=True, role_id=1)
        db.session.add(u)
        db.session.commit()
        assert u.role() == 'admin'

    def tearDown(self):

        """Free resourses."""
        
        db.session.remove()
        db.drop_all()

if __name__ == '__main__':
    unittest.main()
