#! bin/usr/env python
# -*- coding: utf-8 -*-

import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailSender(object):
    """
    This class allow to send email to users
    """

    def send_reset_password_email(self, user, new_password):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Password Reset"
        msg['From'] = "Cycling Official <cycling.official@gmail.com>"
        msg['To'] = user.email
        html = (
            "".join(["Hello, <strong>{}</strong>,",
                     " your password has been reset by Cycling admin",
                     " to: {}"]).format(user.full_name, new_password)
                )
        html_body = MIMEText(html, 'html')

        username = "cycling.official@gmail.com"
        password = "xUP,tB9Y"

        msg.attach(html_body)

        s = smtplib.SMTP('smtp.mandrillapp.com', 587)

        s.login(username, password)
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit()
