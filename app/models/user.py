#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""User table model.

Class User implements model of the user table in database.

"""
from flask_login import UserMixin

from app import db


class User(db.Model, UserMixin):

    """Class represents user model in database.

    Attributes:
        id: Internal user id in database.
        full_name: Full user name.
        email: User email.
        is_active: Flag that indicates whether the user has access to the
        site.
        avatar: Path to the user avatar file.
        role_id: integer number - index of a role ['user', 'admin']

    """

    __tablename__ = 'Users'
    __searchable__ = ['email', 'full_name']

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(64), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    avatar = db.Column(db.String(255))
    role_id = db.Column(db.Integer,
                        default=0,
                        nullable=False)
    roles = ['user', 'admin']

    def role(self):
        return self.roles[int(self.role_id)]

    def __repr__(self):
        return '<User %s>' % self.full_name
