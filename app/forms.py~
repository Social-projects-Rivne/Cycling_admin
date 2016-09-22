#!usr/bin/env python
# -*- coding: utf-8 -*-


class EditUserForm(Form):
    """
    This class represents user edit Form
    """
    id_ = HiddenField("Edit User ID")
    fullName = TextField("User fullname", validators=[DataRequired()])
    email = TextField("User email", validators=[DataRequired()])
    # [password] - will not be implemented as part of form
    # it`s better to make as separate AJAX button
    avatar = TextField("Avatar link", validators=[URL()])
    isActive = BooleanField("Banned/Deleted")
    role_id = SelectBox("Role", choises=[])
    save = SubmitField("Save")
