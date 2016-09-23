#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Application view class for rendering templates.
"""

from flask import render_template

class AdminView(object):

	"""View class for rendering templates."""

	def render_search_page(self):
		"""Render web-page from template and given users_list argument"""
		return render_template('search.html', value)