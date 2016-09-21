#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unittest for User model.

Class TestUser implements unittests for user model.

"""

import unittest

from app import app
from app import db
from app.models.user import User
from config import DATABASE_URI


class TestUser(unittest.TestCase):

    """Test case for user model.

    For test running tables Users and Roles had to be created.

    """

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
        db.create_all()

        self.user = User(full_name='test user', email='test@gmail.com',
                         password='1', is_active=True, avatar='5', role_id='1')

    def tearDown(self):
        db.session.delete(self.user)
        db.session.commit()
        db.session.remove()

    def test_create_user(self):
        """Testing user model.

        At first test tries to create user record in database.
        Than select spesified user from database.

        """
        db.session.add(self.user)
        db.session.commit()

        test_user = User.query.filter_by(full_name='test user').first()
        self.assertEqual(test_user.email, u'test@gmail.com')


if __name__ == '__main__':
    unittest.main()
