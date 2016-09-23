#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    This module is for URL routing.
"""

from app import app
from app.controllers.user_controller import AdminController

controller = AdminController()

@app.route('/')
def hello():
    """Root entry point of application."""
    return "Hello World!"

@app.route('/users/all')
def list_all_users():
    """Return web-page with the list of all users in the database"""
    return controller.get_all_users()
