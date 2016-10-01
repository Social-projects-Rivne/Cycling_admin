#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Application entry point.
"""

from app import app
app.run(port=5555, debug=True)
