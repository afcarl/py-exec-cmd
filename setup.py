# -*- coding: utf-8 -*-
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


CLASSIFIERS=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules'
    ]

setup( 
        name='exec_cmd',
        version='0.1.0',
        description='Command-line execution with timeout',
        long_description = 'See homepage for usage',
        author='Patrick Ng',
        author_email='pn.appdev@gmail.com',
        url='https://github.com/pnpnpn/py-exec-cmd',
        packages=['exec_cmd'],
        install_requires=[],
        #test_suite='tests',
        classifiers=CLASSIFIERS)


