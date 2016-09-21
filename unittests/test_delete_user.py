#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Module for testing deleting user methods (of controller).
"""

import unittest

import sys, os
sys.path.append(os.path.abspath('../'))

from app import app
from app import db
from app.models.User import User
from app.controllers.user_controller import AdminController

class TestDeleteUser(unittest.TestCase):

    """Test case for deleting user methods."""

    def setUp(self):
        """Init database."""
        app.config['TESTING'] = True
        app.config['MYSQL_DATABASE_HOST'] = 'localhost'
        app.config['MYSQL_DATABASE_PORT'] = 3306
        db.create_all()

    def test_delete_user_by_id(self):
        u = User(full_name='test user', email='test@gmail.com',
                         password='1', is_active=True, role_id='1')
        db.session.add(u)
        db.session.commit()
        is_success = AdminController().delete_by_id(1)
        assert is_success

        test_user = User.query.filter_by(id=1).first()
        assert not test_user

    def tearDown(self):

        """Free resourses."""
        
        db.session.remove()

if __name__ == '__main__':
    unittest.main()
