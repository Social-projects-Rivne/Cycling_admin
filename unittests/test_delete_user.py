#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Module for testing deleting user methods (of controller).
"""

import unittest

import sys, os
sys.path.append(os.path.abspath('../'))
basedir = os.path.abspath(os.path.dirname(__file__))

import random
trail = random.randint(100,1000)

from app import app
from app import db
from app.models.user import User
from app.controllers.user_controller import AdminController

class TestDeleteUser(unittest.TestCase):

    """Test case for deleting user methods."""

    def setUp(self):
        """Init database."""
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(basedir, 'test.db')
        db.create_all()

    def test_delete_user_by_id(self):
        u = User(full_name='test user', email='test%s@gmail.com' % trail,
                         password='1', is_active=True, role_id=0)
        db.session.add(u)
        db.session.commit()
        is_success = AdminController().delete_by_id(u.id)
        assert is_success
        assert not u.is_active

    def tearDown(self):

        """Free resourses."""
        
        db.session.remove()
        db.drop_all()

if __name__ == '__main__':
    unittest.main()
