#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    This module is for URL routing.
"""
import json
from flask import Response, request, render_template, redirect, url_for

from app import app
from app.controllers.user_controller import AdminController

_admin_controller = AdminController()


@app.route('/user/<int:user_id>', methods=['DELETE', 'PUT'])
def delete_user(user_id):
    delete_flag = 0 if  request.method == 'DELETE' else 1
    is_success = AdminController().delete_by_id(user_id, delete_flag)
    return  json.dumps({'success':is_success}), 200 if is_success else 404, {'ContentType':'application/json'}

@app.route('/users/all')
def list_all_users():
    """Return web-page with the list of all users in the database"""
    return _admin_controller.get_all_users()


@app.route('/users/<id>/edit', methods=['GET', 'POST'])
def edit_user_page(id):
    """
    This method return edit user page
    """
    return _admin_controller.get_edit_user_page(id, request.form)


@app.route('/users/<int:id>/role_edit', methods=['POST'])
def edit_user_role(id):
    return _admin_controller.change_user_group(id, request.get_json())

@app.route('/users/<int:id>/get_role', methods=['POST'])
def get_user_role(id):
    return _admin_controller.get_user_role_by_id(id)

@app.route('/', methods=['GET'])
def render_base():
    return render_template("form.html", message=None)


@app.route('/users/search', methods=["POST"])
def search():
    Post_data = request.form['search-input']
    return _admin_controller.search_user(Post_data)
