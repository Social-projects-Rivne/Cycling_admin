#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    User controller class for CRUD with User model.
"""

from app.models.User import User 

from app import db

class UserController(object):

    """docstring for UserController"""
    
    def delete_by_id(self, user_id):
        u_to_delete = User.query.filter_by(id=str(user_id)).first()
        print u_to_delete.id
        try:
            db.session.delete(u_to_delete)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False