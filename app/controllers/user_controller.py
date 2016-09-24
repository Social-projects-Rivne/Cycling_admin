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

    def get_user_by_id(self, id):
        """
        Return user object by specified id, None if not found
        """
        return db.session.query(User).get(id)

    def get_edit_user_page(self, id, params):
        """
        This method analyze params and return user edit page
        """
        error = None
        message = None

        user = self.get_user_by_id(id)
        if not user:
            error = "User with specified id is not found."
        else:
            # if params are not None, then it`s put method
            if params:
                user.full_name = params['full_name']
                user.email = params['email']
                user.is_active = params['is_active']
                user.role_id = params['role_id']
                db.session.commit()
                message = "Changes done."

        return self.view.render_edit_user(user=user,
                                          message=message,
                                          error=error)
