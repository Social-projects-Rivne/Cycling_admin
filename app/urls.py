#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    This module is for URL routing.
"""
import json

from flask import request, render_template, redirect, url_for, session
from flask_login import LoginManager, login_user, login_required, logout_user

from app import app
from app.controllers.admin_controller import AdminController
from app.controllers.login_form import LoginForm
from app.models.user import User


login_manager = LoginManager()
# provide default view method for attempts of non logged in
# users to visit protected by login pages:
login_manager.login_view = 'login'
login_manager.init_app(app)

_admin_controller = AdminController()


@app.route('/user/<int:user_id>', methods=['DELETE', 'PUT'])
@login_required
def delete_user(user_id):
    """ This function takes a request and bans/unbans a user """

    delete_flag = 0 if request.method == 'DELETE' else 1
    is_success = AdminController().delete_by_id(user_id, delete_flag)
    return json.dumps({'success': is_success}),\
        200 if is_success else 404,\
        {'ContentType': 'application/json'}


@app.route('/users/<int:user_id>/reset_password', methods=['POST'])
@login_required
def reset_user_password(user_id):
    """ Routing-function for resetting a password for a user """

    json_result, code = _admin_controller.reset_password(user_id)
    return json.dumps(json_result), code, {'ContentType': 'application/json'}


@app.route('/users/all')
@login_required
def list_all_users():
    """Return web-page with the list of all users in the database"""
    return _admin_controller.get_all_users()


@app.route('/users/<user_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_user_page(user_id):
    """
    This method return edit user page
    """
    return _admin_controller.get_edit_user_page(user_id, request.form)


@app.route('/users/<int:user_id>/role_edit', methods=['POST'])
@login_required
def edit_user_role(user_id):
    """ The routing function for editing user's role (user/admin) """
    return _admin_controller.change_user_group(user_id, request.get_json())


@app.route('/users/<int:user_id>/get_role', methods=['POST'])
@login_required
def get_user_role(user_id):
    """ The routing function for retrieving a user's role: user or admin """
    return _admin_controller.get_user_role_by_id(user_id)


@app.route('/', methods=['GET'])
@login_required
def render_base():
    """ Root routing function """
    usr = session['email']
    print usr
    return render_template("list_all_users.html", whoami=usr, message=None)


@app.route('/users/search', methods=["POST"])
@login_required
def search():
    """ Accepts a string and passes it to a search controller """
    post_data = request.form['search-input']
    return _admin_controller.search_user(post_data)


@login_manager.user_loader
def load_user(user_id):
    """ Provide callback function for login_manager which
    reloads the user object from the user ID stored in the
    session. """
    return User.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Return web-page with custom Login form with it's user
    validators. If user's email, password and role are valid
    function logs him in. After successful login redirects to
    the main page. """
    form = LoginForm()
    if request.method == 'POST':
        if form.validate():
            login_user(form.user)
            session['email'] = form.user.email
            print session['email']
            return redirect(url_for('render_base'))
    return render_template('login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    """ This method logs user out clearing the session and redirecting
    to the login page. """
    logout_user()
    return redirect(url_for('login'))
