#!/usr/bin/env python

"""
setup.py
"""

from setuptools import setup, find_packages

setup(
    name='CMservice',
    version='1.0.0',
    description='',
    author='DIRG',
    author_email='dirg@its.umu.se',
    license='Apache 2.0',
    url='',
    packages=find_packages('src/'),
    package_dir={'': 'src'},
    classifiers=['Development Status :: 4 - Beta',
                 'Topic :: Software Development :: Libraries :: Python Modules',
                 'Programming Language :: Python :: 3.4'],
    install_requires=[
        'Flask',
        'pyjwkest',
        'Flask-Babel',
        'Flask-Mako',
        'dataset'],
    zip_safe=False,
)
