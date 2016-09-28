#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    User controller class for CRUD with User model.
"""

import cgi
import sys
import os
import hashlib
import random
import string

from json import dumps

from app import app
from app import db
from app.models.user import User
from app.views.searchview import AdminView
from app.views.view import View


class AdminController(object):
    """docstring for AdminController"""

    _admin_view = AdminView()
    _columns_to_query = (User.id, User.full_name, User.email, 
                         User.is_active, User.avatar, User.role_id)

    def __init__(self):
        """Create instances of models and views"""
        self.view = View()

    def delete_by_id(self, user_id, delete=0):
        u_to_delete = User.query.filter_by(id=str(user_id)).first()
        # print u_to_delete.id
        try:
            # db.session.delete(u_to_delete)
            u_to_delete.is_active = delete
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False

    def get_all_users(self):
        """
        Get list of all users from db and return view rendering function
        """
        users_db_obj = db.session.query(*self._columns_to_query)
        users_list = [user for user in users_db_obj]
        return self.view.render_users_list(users_list)

    def get_user_by_id(self, id):
        """
        Return user object by specified id, None if not found
        """
        return db.session.query(User).get(id)

    def is_last_admin(self):
        return db.session.query(User).filter_by(role_id=1).count() == 1

    def get_edit_user_page(self, id, params):
        """
        This method analyze params and return user edit page
        """
        error = None
        message = None
        # show if message variable is good
        good_message = True

        user = self.get_user_by_id(id)
        if not user:
            error = "User with specified id is not found."
        else:
            if user.role_id == 1 and self.is_last_admin():
                role_disabled = True
            else:
                role_disabled = False
            # if params are not None, then it`s put method
            if params:
                if self.edit_user(self.user, params):
                    message = "Changes done."
                else:
                    message = "Error occurred"
                    good_message = False

        return self.view.render_edit_user(user=user,
                                          message=message,
                                          good_message=good_message,
                                          error=error,
                                          role_disabled=role_disabled)

    def password_to_hash(self, password):
        """
        This method return password hash
        """
        return hashlib.sha512(password.encode()).hexdigest()

    def reset_password(self, email):
        """
        This method reset password of user with specified email
        and send notification email on it
        """
        user = db.session.query(User).filter_by(email=email).first()
        password = self.generate_password()
        hashed_password - self.password_to_hash(password)
        user.password = hashed_password
        self.send_reset_password_email(password)

    def send_reset_password_email(self, password):
        pass

    def generate_password(self, size=24):
        """
        Return random generated password with uppercase letters and digits
        """
        return ''.join(
            random.SystemRandom().choice(
                string.ascii_uppercase + string.digits) for _ in range(24))

    def edit_user(self, user, params):
        """
        Edit given user with given params
        """
        if not params or not user:
            return False

        user.full_name = params['full_name']
        user.email = params['email']
        if 'is_active' in params:
            user.is_active = 0
        else:
            user.is_active = 1
        user.role_id = params['role_id']
        db.session.commit()
        return True

    def search_user(self, value):
        """
        Recieve from input, search for matches and return
        dict of them if exists
        """
        exists = db.session.query(db.exists().
                                  where(User.full_name == value)).scalar()
        exists2 = db.session.query(db.exists().
                                   where(User.email == value)).scalar()
        exists3 = db.session.query(db.exists().
                                   where(User.role_id == value)).scalar()

        search = '%'+value+'%'

        if exists:
            users_db_obj = db.session.query(*self._columns_to_query).filter\
              (User.full_name.like(search))
            result = [row for row in users_db_obj]
            return self._admin_view.render_search_page(result)
        elif exists2:
            users_db_obj = db.session.query(*self._columns_to_query).filter\
              (User.email.like(search))
            result = [row for row in users_db_obj]
            return self._admin_view.render_search_page(result)
        elif exists3:
            users_db_obj = db.session.query(*self._columns_to_query).filter_by\
              (role_id=value)
            result = [row for row in users_db_obj]
            return self._admin_view.render_search_page(result)
        else:
            return self._admin_view.render_search_page("Matches doesn't exist")

    def change_user_group(self, user_id, params):
        try:
            u_id = str(user_id)
            u_role = int(params['user_role'])
        except:
            return self._response_for_ajax(msg='Unable to parse input \
                                           parameters in query.',
                                           status_code=400)

        try:
            user_to_change = User.query.filter_by(id=u_id).first()
        except:
            return self._response_for_ajax(msg='Unable select user by id.',
                                           status_code=400)

        if user_to_change.role_id == 1 and self.is_last_admin():
            return self._response_for_ajax(msg='OK', status_code=200)

        if user_to_change.role_id == u_role:
            return self._response_for_ajax(msg='OK', status_code=200)

        user_to_change.role_id = u_role

        try:
            db.session.commit()
        except:
            return self._response_for_ajax(msg='Unable to change user role.',
                                           status_code=500)

        return self._response_for_ajax(msg='OK', status_code=200)

    def get_user_role_by_id(self, user_id):
        """Return user role by id for quick role change."""
        try:
            u_id = str(user_id)
        except:
            return self._response_for_ajax(msg='Unable to parse input \
                                           parameters in query.',
                                           status_code=400)

        cur_user = User.query.filter_by(id=u_id).first()
        return self._response_for_ajax(msg=cur_user.role(), status_code=200)

    def _response_for_ajax(self, msg, status_code):
        """Quick forming response for ajax methods."""
        return (dumps({'message': msg}),
                status_code,
                {'ContentType': 'application/json'})
