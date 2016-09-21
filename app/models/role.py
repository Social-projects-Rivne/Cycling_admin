#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    This module implements roles table model.
"""

from app import db

class Role(db.Model):

    """Class represents user model in database."""

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
