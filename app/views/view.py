#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Application view class for rendering templates.
"""

from flask import render_template

class View(object):

	"""View class for rendering templates."""

	def render_users_list(self, users_list):
		"""Render web-page from template and given users_list argument"""
		return render_template('list_all_users.html', users_list=users_list)