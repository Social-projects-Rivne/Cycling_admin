#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    This module is for URL routing.
"""

from app import app


@app.route('/')
def hello():
    """Root entry point of application."""
    return "Hello World!"


@app.route('/users/<id>/edit', methods=['GET', 'PUT'])
def edit_user_page(id):
    """
    This method return edit user page
    """
    controller = EditUserController(id, put_dict=request.form)
    return controller.render_template()
