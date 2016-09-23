#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module for parsing configuration file.

Configuration file should have name 'config.ini'.
Also 'config.ini' file should be in the same catalog with config.py file.

Example of configuraion file:
[DATABASE]
uri: mysql://root:123@172.17.0.3/CYCLINGDB

"""

#from configparser import SafeConfigParser
from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read('config.ini')

DATABASE_URI = config.get('DATABASE', 'uri')
