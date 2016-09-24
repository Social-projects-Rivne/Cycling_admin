#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""User table model.

Class User implements model of the user table in database.

"""

from app import db
from app import app
from app.models.role import Role
from config import DATABASE_URI

class User(db.Model):

    """Class represents user model in database.

    Attributes:
        id: Internal user id in database.
        full_name: Full user name.
        email: User email.
        is_active: Flag that indicates whether the user has access to the
        site.
        avatar: Path to the user avatar file.
        role_id: link to the user role table.

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
                        db.ForeignKey('Roles.id',
                                      use_alter=True,
                                      name='fk_role_id'),
                        nullable=False)

    # def __init__(self, **kwargs):
    #     self.full_name = kwargs.get('full_name')
    #     self.email = kwargs.get('email')
    #     self.password = kwargs.get('password')
    #     self.is_active = kwargs.get('is_active')
    #     self.avatar = kwargs.get('avatar')
    #     self.role_id = kwargs.get('role_id')

    def __repr__(self):
        return '<User %s>' % self.full_name

class UserHandler(object):

    """Purpose of this class is to CRUD data about Users from DB"""

    def __init__(self):
        """Parse mysql credentials from config file and run db"""
        app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
        db.create_all()

    def select_all_users(self):
        """
        Send select * query to the db except password column, return list
        """
        self.users_db_obj = User.query.add_columns('id', 'full_name', 'email',
         'is_active', 'avatar', 'role_id')
        self.result = [row[1:] for row in self.users_db_obj]
        return self.result
