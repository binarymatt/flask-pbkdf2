from __future__ import absolute_import
__version__ = '0.1.0'

import os
import binascii
import hashlib

from pbkdf2 import pbkdf2_hex
def safe_str_cmp(a, b):
    if len(a) != len(b):
        return False
    rv = 0
    for x, y in zip(a, b):
        rv |= ord(x) ^ ord(y)
    return rv == 0

class Pbkdf2(object):
    hashfunc = hashlib.sha256
    def __init__(self, app=None):
        self.app = app
        self.iterations = app.config.get('PBKDF2_ITERATIONS', 1000)

    def check_password(self, password, encoded):
        algorithm, iterations, salt, hash_val = encoded.split('$', 3)
        assert algorithm == "pbkdf2_sha256"
        #expected = pbkdf2_hex(password, salt, int(iterations), hashfunc=self.hashfunc)
        expected = self.make_password(password, salt, int(iterations))
        return safe_str_cmp(encoded, expected)

    def make_password(self, password, salt=None, iterations=None):
        if not salt:
            salt = self.generate_salt()
        if not iterations:
            iterations = self.iterations
        hash_val = pbkdf2_hex(password, salt, iterations, hashfunc=self.hashfunc)
        return '%s$%s$%s$%s' % ('pbkdf2_sha256', iterations, salt, hash_val)

    def generate_salt(self, keylen=15):
        return binascii.b2a_hex(os.urandom(keylen))
