#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    User controller class for CRUD with User model.
"""

import cgi
import sys, os
sys.path.append(os.path.abspath('..//..//'))
from app import app
from app import db
from app.models.User import User
from config import DATABASE_URI
from app.views.searchview import AdminView

app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_URI

class AdminController(object):
    """docstring for UserController"""
    _admin_view = AdminView()

    def search_user(self, value):
        exists = db.session.query(db.exists().where(User.full_name == value)).scalar()
        exists2 = db.session.query(db.exists().where(User.email == value)).scalar()
        exists3 = db.session.query(db.exists().where(User.role_id == value)).scalar()
        if exists:   
            result = db.session.query(User).filter_by(full_name = value).all()
            return _admin_view.render_search_page(result)
        elif exists2:
            result = db.session.query(User).filter_by(email = value).all()
            return admin_view.render_search_page(result)
        elif exists3:
            result = db.session.query(User).filter_by(role_id = value).all()
            return admin_view.render_search_page(result)
        else:
            return "Error input"

if __name__ == '__main__':
    pass
    
    