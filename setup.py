#!/usr/bin/env python
# -*- coding: utf-8; mode: python -*-

import re
import codecs
from setuptools import setup, find_packages

def read_file(fname):
    with codecs.open(fname, 'r', 'utf-8') as f:
        return f.read()

def find_meta(meta):
    """
    Extract __*meta*__ from META_FILE.
    """
    meta_match = re.search(
        r"^__{meta}__\s*=\s*['\"]([^'\"]*)['\"]".format(meta=meta),
        META_FILE
        , re.M )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))

NAME             = 'konfig'
REQUIRES         = ['configparser', 'six']
TESTS_REQUIRES   = REQUIRES + []
META_FILE        = read_file('konfig/__init__.py')
LONG_DESCRIPTION = [ read_file(n) for n in ['README.rst', 'CHANGES.txt']]

setup(name                   = NAME
      , version              = find_meta('version')
      , description          = find_meta('description')
      , long_description     = '\n\n'.join(LONG_DESCRIPTION)
      , url                  = find_meta('url')
      , author               = find_meta('author')
      , author_email         = find_meta('author_email')
      , license              = find_meta('license')
      , keywords             = find_meta('keywords')
      , packages             = find_packages()
      , include_package_data = True
      , install_requires     = REQUIRES
      # unfortunately test is not supported by pip (only 'setup.py test')
      , tests_require        = TESTS_REQUIRES
      , test_suite           = NAME
      , zip_safe             = False
      , classifiers          = [
          "Programming Language :: Python"
          , "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)"
          , "Development Status :: 5 - Production/Stable"
          , ]
      , )
