#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    This module implements user table model.
"""

from app import db


class User(db.Model):
    """Class represents user model in database."""
    __tablename__ = 'users'
    __searchable__ = ['email', 'full_name', 'role_id']

    user_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(64), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    avatar = db.Column(db.String(255))
    role_id = db.Column(db.Integer,
                        db.ForeignKey('roles.id',
                                      use_alter=True,
                                      name='fk_role_id'),
                        nullable=False)

    def __init__(self, **kvargs):
        self.full_name = kvargs.get('full_name')
        self.email = kvargs.get('email')
        self.password = kvargs.get('password')
        self.is_active = kvargs.get('is_active')
        self.avatar = kvargs.get('avatar')
        self.role_id = kvargs.get('role_id')

    def __repr__(self):
        return '<User %s>' % self.full_name
