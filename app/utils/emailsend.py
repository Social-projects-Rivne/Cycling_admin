#! bin/usr/env python
# -*- coding: utf-8 -*-

import os

from flask import render_template, request


class EmailSender(object):
    """
    This class allow to send email to users
    """

    def send_reset_password_email(self, user, new_password):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-Postmark-Server-Token": "f2b33489-0ba6-4eb5-8372-dd394b960d22"
        }
        template = render_template(
            "reset_password_email.html",
            user=user, new_password=new_password)
        print template
        data = "".join([
            "{'From': 'cycling.official@email.ua',",
            " 'To': '", str(user.email), "',",
            " 'Subject': 'Password Reset',",
            " 'HtmlBody': '", str(template), "'}",
        ])

        r = requests.post(
            "https://api.postmarkapp.com/email",
            headers=headers,
            data=data)
        print r.text
