#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    This module is for URL routing.
"""
import json
from flask import request, render_template

from app import app
from app.controllers.user_controller import AdminController

_admin_controller = AdminController()

@app.route('/user/<int:user_id>', methods=['DELETE', 'PUT'])
def delete_user(user_id):
    """ This function takes a request and bans/unbans a user """

    delete_flag = 0 if request.method == 'DELETE' else 1
    is_success = AdminController().delete_by_id(user_id, delete_flag)
    return json.dumps({'success': is_success}),\
        200 if is_success else 404,\
        {'ContentType': 'application/json'}


@app.route('/users/<int:user_id>/reset_password', methods=['POST'])
def reset_user_password(user_id):
    """ Routing-function for resetting a password for a user """

    json_result, code = _admin_controller.reset_password(user_id)
    return json.dumps(json_result), code, {'ContentType': 'application/json'}


@app.route('/users/all')
def list_all_users():
    """Return web-page with the list of all users in the database"""
    return _admin_controller.get_all_users()


@app.route('/users/<user_id>/edit', methods=['GET', 'POST'])
def edit_user_page(user_id):
    """
    This method return edit user page
    """
    return _admin_controller.get_edit_user_page(user_id, request.form)

@app.route('/users/<int:user_id>/role_edit', methods=['POST'])
def edit_user_role(user_id):
    """ The routing function for editing user's role (user/admin) """
    return _admin_controller.change_user_group(user_id, request.get_json())


@app.route('/users/<int:user_id>/get_role', methods=['POST'])
def get_user_role(user_id):
    """ The routing function for retrieving a user's role: user or admin """
    return _admin_controller.get_user_role_by_id(user_id)


@app.route('/', methods=['GET'])
def render_base():
    """ Root routing function """
    return render_template("list_all_users.html", message=None)

@app.route('/users/search', methods=["POST"])
def search():
    """ Accepts a string and passes it to a search controller """
    post_data = request.form['search-input']
    return _admin_controller.search_user(post_data)
    