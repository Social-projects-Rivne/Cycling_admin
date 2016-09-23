#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    User controller class for CRUD with User model.
"""

from app.models.user import User, UserHandler
from app.views.view import View
from app import db

class AdminController(object):

    """docstring for AdminController"""

    def __init__(self):
        """Create instances of models and views"""
        self.users_model = User()
        self.users_model = UserHandler()
        self.view = View()

    def delete_by_id(self, user_id):
        u_to_delete = User.query.filter_by(id=str(user_id)).first()
        # print u_to_delete.id
        try:
            db.session.delete(u_to_delete)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False

    def get_all_users(self):
        """
        Get list of all users from db via User model and return view 
        rendering function
        """
        _users_list = self.users_model.select_all_users()
        return self.view.render_users_list(_users_list)
