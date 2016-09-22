#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    This module is for URL routing.
"""

from flask import Response, json, jsonify, request
from app import app
from app.controllers.user_controller import AdminController


@app.route('/')
def hello():
    """Root entry point of application."""
    return "Hello World!"

@app.route('/users/search', methods=["POST", "GET"])
def search():
	tmp = request.get_json()
	tmp['chototam'] = "value"
	return jsonify(tmp)