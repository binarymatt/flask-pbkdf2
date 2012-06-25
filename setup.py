'''
    Flask-pbkdf2
    ------------

    Flask application that provides pbkdf2 hashing
'''

from setuptools import setup

setup(
    name='Flask-Pbkdf2',
    version='0.1',
    url='https://github.com/binarydud/flask-pbkdf2',
    license='BSD',
    author='Matt George',
    author_email='mgeorge@gmail.com',
    description='pbkdf2 hashing for Flask.',
    long_description=__doc__,
    py_modules=['flask_pbkdf2'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'simple-pbkdf2'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='test_pbkdf2'
)

