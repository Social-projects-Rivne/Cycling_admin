#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    This module is for URL routing.
"""
from flask import render_template, redirect, url_for, request

from app import app
from app.controllers.user_controller import AdminController

controller = AdminController()


@app.route('/')
def index():
    """Root entry point of application."""
    return render_template('index.html',
                           greeting='Hello from index.html template')


@app.route('/user/<int:user_id>', methods=['DELETE'])
# @login_required
def delete_user(user_id):
    is_success = AdminController.delete_by_id(user_id)
    message = 'Deleting the user with id=%s: %s' % (user_id, is_success)
    return redirect(url_for('index'), message=message)


@app.route('/users/all')
def list_all_users():
    """Return web-page with the list of all users in the database"""
    return controller.get_all_users()


@app.route('/users/<id>/edit', methods=['GET', 'PUT'])
def edit_user_page(id):
    """
    This method return edit user page
    """
    return controller.get_edit_user_page(id, request.form)
