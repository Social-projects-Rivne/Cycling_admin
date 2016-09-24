"""
This controller used to handle user edit
"""

from flask import render_template


class EditUserController(object):
    """
    This controller handle all work with edit user page
    """

    def __init__(self, id, put_dict=None):
        self.id = id
        self.target_user = db.session.query(User).get(self.id)
        if target_user is not None:
            if put_dict is not None:
                self._handle_put(put_dict)

    def _handle_put(self, put_dict):
        """
        This method validate put data and update target user fields
        """
        # input validaton
        if 'full_name' not in put_dict
        or 'email' not in put_dict
        or 'is_active' not in put_dict
        or 'role_id' not in put_dict:
            _handle_error()
        # update
        self.target_user.full_name = put_dict['full_name']
        self.target_user.full_name = put_dict['email']
        self.target_user.full_name = put_dict['is_active']
        self.target_user.full_name = put_dict['role_id']
        db.session.commit()
        _handle success()

    def _handle_error(self):
        self.message = "Дані користувача успішно змінено."

    def _handle_error(self):
        self.error = "Не вірні дані."

    def render_template(self, code=0):
        """
        This method return html
        """
        return render_template('edit_user.html',
                               user=self.target_user,
                               message=self.message,
                               error=self.error)
