#/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Test all users listing at url /users/all
"""

import unittest
from mock import patch

from app import app
from app.models.user import User
from app.controllers.user_controller import AdminController


class TestUsersListing(unittest.TestCase):

	"""
	This class tests controller and view template for url /users/all in
	next cases:
	- db is unreachable;
	- there is some user in the db (faked by mock);
	- there are no users in the database.
	"""

	def setUp(self):
		pass

	def tearDown(self):
		pass

	@patch('app.controllers.user_controller.db')
	def test_controller_with_fake_usr(self, db):
		"""
		Fake db output with mock and check if it is processed by controller
		and template.
		"""
		#			id, full_name, email, is_active, avatar, role_id
		fake_usr = [(110, 'Hillary Trump', 'test@gmail.com', 1, 'None', 1)]
		db.session.query.return_value.all.return_value = fake_usr
		with app.test_client() as test_client:
			responce = test_client.get('/users/all')
			data = responce.data
			self.assertIn('Hillary Trump', data)
			self.assertIn('admin', data)

	@patch('app.controllers.user_controller.db')
	def test_controller_with_empty_db(self, db):
		"""
		Imitate situation when there is no any user available in the db and
		sqlalchemy output becomes an empty list []. Message 'There are no 
		users in the database' instead of users table is expected as default
		behavior in this case.
		"""
		db.session.query.return_value.all.return_value = []
		with app.test_client() as test_client:
			responce = test_client.get('/users/all')
			data = responce.data
			self.assertIn('There are no users in the database.', data)

	def test_unavailable_db(self):
		"""
		Check if "Can not access database" message appears if db is 
		unavailable.
		"""
		#break db uri to call exception inside controller
		app.config['SQLALCHEMY_DATABASE_URI'] = ''
		with app.test_client() as test_client:
			responce = test_client.get('/users/all')
			data = responce.data
			self.assertIn("Can not access database.", data)
			self.assertNotIn('<table class="table">', data)


if __name__ == '__main__':
	unittest.main()
