#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    User controller class for CRUD with User model.
"""



import cgi
import sys, os

from app import app
from app import db
from app.models.user import User, UserHandler
from app.views.searchview import AdminView
from app.views.view import View


class AdminController(object):
    """docstring for AdminController"""
    
    _admin_view = AdminView()
    
    def __init__(self):
        """Create instances of models and views"""
        self.users_model = User()
        self.users_model = UserHandler()
        self.view = View()

    def delete_by_id(self, user_id):
        u_to_delete = User.query.filter_by(id=str(user_id)).first()
        # print u_to_delete.id
        try:
            db.session.delete(u_to_delete)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False

    def get_all_users(self):
        """
        Get list of all users from db via User model and return view
        rendering function
        """
        _users_list = self.users_model.select_all_users()
        return self.view.render_users_list(_users_list)

    def search_user(self, value):
        exists = db.session.query(db.exists().where(User.full_name == value)).scalar()
        exists2 = db.session.query(db.exists().where(User.email == value)).scalar()
        exists3 = db.session.query(db.exists().where(User.role_id == value)).scalar()
        if exists:   
            result = db.session.query(User).filter_by(full_name = value).all()
            return self._admin_view.render_search_page(result)
        elif exists2:
            result = db.session.query(User).filter_by(email = value).all()
            return self._admin_view.render_search_page(result)
        elif exists3:
            result = db.session.query(User).filter_by(role_id = value).all()
            return self._admin_view.render_search_page(result)
        else:
            return "Error input"

if __name__ == '__main__':
    pass

