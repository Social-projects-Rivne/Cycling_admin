#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    This module is for URL routing.
"""

from flask import Response, json, jsonify, request, render_template
from app import app
from app.controllers.user_controller import AdminController

_admin_controller = AdminController()

@app.route('/')
def hello():
    """Root entry point of application."""
    return "Hello World!"

@app.route('/users/search', methods=['GET'])
def render_base():
	return render_template("form.html")

@app.route('/users/search', methods=["POST"])
def search():
	Post_data = request.form['search-input']
	return _admin_controller.search_user(Post_data)