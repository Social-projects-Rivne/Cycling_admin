#! bin/usr/env python
# -*- coding: utf-8 -*-
"""
This module provide all work with email sends
"""

import requests
from flask import render_template

from config import API_TOKEN, MAIL_FROM  # pylint: disable=import-error


def send_reset_password_email(user, new_password):
    """
    Send email about password reset to target user email
    """
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-Postmark-Server-Token": API_TOKEN
    }
    # we need to render email html template from file
    template = render_template(
        "reset_password_email.html",
        user=user, new_password=new_password)
    # creating request data
    data = "".join([
        "{'From': '", MAIL_FROM, "',",
        " 'To': '", str(user.email), "',",
        " 'Subject': 'Password Reset',",
        " 'HtmlBody': '", str(template.encode('utf-8')), "'}",
    ])
    requests.post(
        "https://api.postmarkapp.com/email",
        headers=headers,
        data=data)
