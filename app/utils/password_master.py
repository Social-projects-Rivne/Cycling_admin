#! usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module makes password hashing and unhashing operations
"""
import hashlib
import string
import random


class PasswordMaster(object):
    """
    This class provide all work with passwords hash and checks
    """

    # this const used to make salt in hash
    SALT_NAME = 'mrsalt'

    def generate_salt(self, length=10):
        """
        This method generate salt for SHA512 encrypiton
        default length of salt is 10
        """
        return "".join(
            random.SystemRandom().choice(
                string.ascii_uppercase + string.digits) for _ in range(length))

    def hash_password(self, password, salt=None):
        """
        Hash given password with sha512 and salt
        """
        sha512 = hashlib.sha512()
        if not salt:
            salt = self.generate_salt()
        sha512.update("".join([
            salt.encode('utf8'),
            self.SALT_NAME.encode('utf8'),
            password.encode('utf8')
        ]))
        return "".join([salt, self.SALT_NAME, sha512.hexdigest()])

    def check_password(self, password_to_check, hashed_password):
        """
        This method check if given password is same as hashed password
        """
        # getting salt from hashed password
        salt = hashed_password.split(self.SALT_NAME)[0]
        return self.hash_password(password_to_check, salt) == hashed_password
