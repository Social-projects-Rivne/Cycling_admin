#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Module for testing deleting user methods (of controller).
"""

import unittest
from mock import patch
from mock import Mock

import sys, os
sys.path.append(os.path.abspath('../'))
basedir = os.path.abspath(os.path.dirname(__file__))

from app import app
from app.controllers.admin_controller import AdminController

class TestDeleteUser(unittest.TestCase):

    """Test case for deleting user methods."""

    def setUp(self):
        pass
       
    def test_delete_user_by_id(self):
        """Test user controllier method that deactivates or activates a user."""
        with patch('app.controllers.admin_controller.User') as mock_model:

            mock_model.query.filter_by.return_value.\
                first.return_value.\
                is_active = 1
            # print mock_model.query.filter_by().first().is_active
            is_success = AdminController().delete_by_id(user_id=1)
            assert is_success
            # print mock_model.query.filter_by().first().is_active
            assert not mock_model.query.filter_by().first().is_active
            is_success = AdminController().delete_by_id(user_id=1, delete=1)
            assert is_success
            # print mock_model.query.filter_by().first().is_active
            assert mock_model.query.filter_by().first().is_active

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
