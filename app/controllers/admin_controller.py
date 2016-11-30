#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    User controller class for CRUD with User model.
"""

import hashlib
import random
import string
import traceback

from json import dumps

from app import db
from app.utils.emailsend import send_reset_password_email
from app.models.user import User
from app.views.adminview import AdminView


class AdminController(object):
    """docstring for AdminController"""

    _columns_to_query = (User.id, User.full_name, User.email,
                         User.is_active, User.avatar, User.role_id)

    def __init__(self):
        """Create instances of models and views"""
        self.admin_view = AdminView()

    def delete_by_id(self, user_id, delete=0):
        """ Bans or unbans a user """
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
        output = db.session.query(*self._columns_to_query).all()
        if output == []:
            output = "There are no users in the database."

        return self.admin_view.render_users_list(output)

    def get_user_by_id(self, user_id):
        """
        Return user object by specified user_id, None if not found
        """
        return db.session.query(User).get(user_id)

    def is_last_admin(self):
        return db.session.query(User).filter_by(role_id=1).count() == 1

    def get_edit_user_page(self, user_id, params):
        """
        This method analyze params and return user edit page
        """
        error = None
        message = None
        # show if message variable is good
        good_message = True

        user = self.get_user_by_id(user_id)
        if not user:
            error = "User with specified user_id is not found."
        else:
            role_disabled = bool(user.role_id == 1 and self.is_last_admin())

            # if params are not None, then it`s put method
            if params:
                if self.edit_user(user, params):
                    message = "Changes done."
                else:
                    message = "Error occurred"
                    good_message = False
        return self.admin_view.render_edit_user(user=user,
                                                message=message,
                                                good_message=good_message,
                                                error=error,
                                                role_disabled=role_disabled)

    def password_to_hash(self, password):
        """
        This method return password hash
        """
        return hashlib.sha512(password.encode()).hexdigest()

    def reset_password(self, user_id):
        """
        This method reset password of user with specified email
        and send notification email on it
        """
        user = db.session.query(User).filter_by(id=user_id).first()
        password = self.generate_password()
        hashed_password = self.password_to_hash(password)
        # print password, " --> ", hashed_password
        user.password = hashed_password
        # print "Trying to reset password of ", user.full_name
        db.session.commit()
        try:
            send_reset_password_email(user, password)
            return {'result': 'success'}, 200
        except Exception, error:
            print "EXCEPTION: ", error
            traceback.print_exc()
            return {'result': 'error'}, 404

    def generate_password(self, size=24):
        """
        Return random generated password with uppercase letters and digits
        """
        return ''.join(
            random.SystemRandom().choice(
                string.ascii_uppercase + string.digits) for _ in range(size))

    def edit_user(self, user, params):
        """
        Edit given user with given params
        """
        if not params or not user:
            return False

        user.full_name = params['full_name']
        user.email = params['email']
        user.avatar = params.get('avatar_url', None)
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
        dict of them if exists.
        """
        search = '%'+value+'%'
        result = db.session.query(*self._columns_to_query).filter(
            User.full_name.like(search)).all()
        if not result:
            result = db.session.query(*self._columns_to_query).filter(
                User.email.like(search)).all()
            if not result:
                result = "Matches doesn't exist"
        return self.admin_view.render_users_list(result)

    def change_user_group(self, user_id, params):
        """Change user's role: user or admin"""
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
