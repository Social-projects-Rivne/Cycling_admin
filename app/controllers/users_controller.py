# -*- coding: utf-8 -*-

from app.models.users import User

from app import db

def delete_by_id(user_id):
    u_to_delete = User.query.filter_by(id=str(user_id)).first()
    print u_to_delete
    try:
        db.session.delete(u_to_delete)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False