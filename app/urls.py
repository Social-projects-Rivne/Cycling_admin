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
