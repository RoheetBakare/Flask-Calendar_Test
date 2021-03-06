# -*- coding: utf-8 -*-

from setuptools import setup

project = "My test Cloned Repo Project"

setup(
    name=project,
    version='0.1',
    url='https://github.com/imwilsonxu/fbone',
    description='Fbone (Flask bone) is a Flask (Python microframework) template/bootstrap/boilerplate application.',
    author='RB456789',
    author_email='imwilsonxu@gmail.com',
    packages=["fbone"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'Flask-Admin',
        'Flask-DebugToolbar',
        'Flask-SQLAlchemy',
        'Flask-WTF',
        'Flask-Script',
        'Flask-Babel',
        'Flask-Testing',
        'Flask-Mail',
        'Flask-Cache',
        'Flask-Login',
        'Flask-OpenID',
        'nose',
        'mysql-python',
    ],
    test_suite='tests',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries'
    ]
)

# this is a test message for git push exercise 