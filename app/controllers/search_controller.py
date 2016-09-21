#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module add posibility to search users by admin.
"""

from app import app
from app import db
from app.models.User import User


class SearchUser():
    """Class for searching users by admin."""
    def setUp(self):
        """Init database."""
        app.config['SQLALCHEMY_DATABASE_URI']='mysql://denny:isurrender@localhost/local_db'
        db.create_all()
        self.user = User(full_name='John Doe', email='John@gmail.com',
                                 password='qwerty', is_active=True, avatar='ava', role_id='1')

    def tearDown(self):
        """Free resourses."""
        db.session.delete(self.user)
        db.session.commit()
        db.session.remove()

    def search_create_user(self):
        db.session.add(self.user)
        db.session.commit()
        search_user = User.query.filter_by(full_name='test user').first()
        return search_user

if __name__ == '__main__':
    
    setUp()
    search_create_user()
