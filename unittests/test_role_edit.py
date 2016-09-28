#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unittest for role change method.

Class TestRoleEdit implements unittests for controller method
that quick changes user role, and method that quick get user role.

"""

from unittest import TestCase
from unittest import main
from mock import patch
from json import loads

from app.controllers.user_controller import AdminController


class TestRoleEdit(TestCase):

    """Test case for edit role method in user controller."""

    def test_get_user_by_id(self):
        """Test user controllier method that returns user role by id."""
        with patch('app.controllers.user_controller.User') as mock:
            mock.query.filter_by.return_value.first.return_value.role.return_value = u'admin'
            c = AdminController()
            result = c.get_user_role_by_id(1)
            message = loads(result[0])
            self.assertEqual(message['message'], u'admin')


if __name__ == '__main__':
    main()