"""Unittest for User model.

Class TestUser implements unittests for user model.

"""

import unittest

from app import app
from app import db

from app.models.user import User
from app.controllers.user_controller import AdminController
from config import DATABASE_URI


class TestEditUser(unittest.TestCase):
    """
    This test try to edit user with AdminController class

    author: Olexii Lykianchyk
    """

    def setUp(self):
        """
        Create new user in database
        """
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
        db.create_all()

        self.user = User(full_name='test user', email='test@gmail.com',
                         password='1', is_active=True, role_id='1')

        # future edit params
        self.params = {
            'full_name': 'new test user name',
            'email': 'new_test_mail@gmail.com',
            "is_active": True,
            "role_id": 1
        }

        db.session.add(self.user)
        db.session.commit()

    def test_edit_user(self):
        controller = AdminController()
        self.assertTrue(controller.edit_user(self.user, self.params))
        self.assertEqual(self.user.full_name, self.param['full_name'])
        self.assertEqual(self.user.email, self.param['email'])
        self.assertEqual(self.user.is_active, self.param['is_active'])
        self.assertEqual(self.user.role_id, self.param['role_id'])

    def tearDown(self):
        """
        Clearing db
        """
        db.session.delete(self.user)
        db.session.commit()
