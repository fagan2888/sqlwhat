#!/usr/bin/env python

import re
import ast
from os import path
from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

PACKAGE_NAME = 'sqlwhat'
HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, 'README.md'), encoding='utf-8') as fp:
    README = fp.read()
with open(path.join(HERE, PACKAGE_NAME, '__init__.py'), 'rb') as fp:
    VERSION = str(ast.literal_eval(_version_re.search(
        fp.read().decode('utf-8')).group(1)))

setup(
	name=PACKAGE_NAME,
	version=VERSION,
	packages=['sqlwhat', 'sqlwhat.checks'],
	install_requires=['protowhat', 'antlr-plsql>=0.1.0', 'antlr-tsql>=0.1.0'],
        description = 'Submission correctness tests for SQL',
        long_description=README,
        long_description_content_type='text/markdown',
        license='GNU version 3',
        author='Michael Chow',
        author_email='michael@datacamp.com',
        maintainer='Filip Schouwenaars',
        maintainer_email='filip@datacamp.com',
        url = 'https://github.com/datacamp/sqlwhat')
