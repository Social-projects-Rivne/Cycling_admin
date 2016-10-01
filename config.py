#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module for parsing configuration file.

Configuration file should have name 'config.ini'.
Also 'config.ini' file should be in the same catalog with config.py file.

Example of configuraion file:

[DataBase]
ENGINE: mysql
DB_USER: user_name
PASSWORD: user_password
HOST: localhost
PORT: 3306
NAME: CYCLINGDB
[MailSender]
API_TOKEN: f2b33489-0ba6-4eb5-8372-dd394b960d22
MAIL_FROM: cycling.official@email.ua
"""

from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read('./config.ini')

MAIL_SENDER = "MailSender"

API_TOKEN = config.get(MAIL_SENDER, 'API_TOKEN')
MAIL_FROM = config.get(MAIL_SENDER, 'MAIL_FROM')

ENGINE = config.get('DataBase', 'ENGINE')
DB_USER = config.get('DataBase', 'DB_USER')
PASSWORD = config.get('DataBase', 'PASSWORD')
HOST = config.get('DataBase', 'HOST')
PORT = config.get('DataBase', 'PORT')
DB_NAME = config.get('DataBase', 'NAME')

DATABASE_URI = '%s://%s:%s@%s:%s/%s' % (ENGINE,
                                        DB_USER,
                                        PASSWORD,
                                        HOST,
                                        PORT,
                                        DB_NAME,)
