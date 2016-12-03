#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import TextField, PasswordField, validators

from app.models.user import User
from app.utils.password_master import PasswordMaster


class LoginForm(Form, PasswordMaster):
    """ This class provides logic for custom form on login.html and for /login
    url view.

    Method validate(self) checks in the database email and password,
    user role (admin or non-admin, because access for this admin-website is
    provided only for admin users) and user status (is it active or deleted).
    When some errors are found they're attached to the form's individual
    fields and are shown for the user after page refresh. Also existence of
    any single error causes validate method to return False and to block any
    additional advance to the web-site. If everything is ok it returns True
    and attaches user data from the database query to the current instance of
    the form, which later is used in urls.py by flask-login and it's
    LoginManager.

    LoginForm inherits from PasswordMaster method password_check which creates
    salted SHA512 hash for entered in input password and compares it with
    user's hashed password from the database.

    """
    email = TextField('Email: ', [validators.Required()])
    password = PasswordField('Password: ', [validators.Required()])

    def __init__(self, *args, **kwargs):
        # Form.__init__(self, *args, **kwargs)
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        """ This method validates user input and returns False if some errors
        are found, otherwise returns True.

        Next validation is done:
            - are inputs not empty?
            - does user with given email exist?
            - is entered password correct?
            - is user admin?
            - is user active?
        """
        rv = Form.validate(self)
        if not rv:
            return False

        user = User.query.filter_by(
            email=self.email.data).first()

        if user is None:
            self.email.errors.append('Unknown email')
            return False

        if self.check_password(self.password.data, user.password) == False:
            self.password.errors.append('Invalid password')
            return False

        if not int(user.role_id) == 1:
            self.email.errors.append("You don't have permission for access")
            return False

        if not user.is_active:
            self.email.errors.append("Your account was suspended")
            return False

        self.user = user
        return True
