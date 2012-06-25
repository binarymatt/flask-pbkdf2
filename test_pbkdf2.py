import unittest

import flask
from flask_pbkdf2 import Pbkdf2

class Pbkdf2TestCase(unittest.TestCase):
    def setUp(self):
        app = flask.Flask(__name__)
        app.config['ITERATIONS'] = 1000
        self.pbkdf2 =Pbkdf2(app)

    def test_check_password(self):
        encoded = 'pbkdf2_sha256$1000$tablesalt$8cc051c0f3c5f2e20cdd8fd85d1eb02a911381ff0fa217c0'
        self.assertTrue(self.pbkdf2.check_password('test',encoded))
        with self.assertRaises(AssertionError):
            self.pbkdf2.check_password('test','sha1$1000$tablesalt$8cc051c0f3c5f2e20cdd8fd85d1eb02a911381ff0fa217c0')

    def test_make_password(self):
        self.assertEqual('pbkdf2_sha256$1000$tablesalt$8cc051c0f3c5f2e20cdd8fd85d1eb02a911381ff0fa217c0',self.pbkdf2.make_password('test',salt='tablesalt'))

if __name__ == '__main__':
    unittest.main()
