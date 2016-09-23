#!usr/bin/env python
# -*- coding: utf-8 -*-


class EditUserForm(Form):
    """
    This class represents user edit Form
    """
    id_ = HiddenField("Edit User ID")
    fullName = TextField("User fullname", validators=[DataRequired()])
    email = TextField("User email", validators=[DataRequired()])
    ban = BooleanField("Banned/Deleted")
    # TODO roles upload
    role = SelectBox("Role", choises=[])
