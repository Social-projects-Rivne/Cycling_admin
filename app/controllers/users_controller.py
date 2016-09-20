# -*- coding: utf-8 -*-

from app.models.User import User

from app import db

def delete_by_id(user_id):
    u_to_delete = User.query.filter_by(id=user_id).first()
    try:
        db.session.delete(u_to_delete)
        db.session.commit()
        return True
    except:
        db.rollback()
        return False