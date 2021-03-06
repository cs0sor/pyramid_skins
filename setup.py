##############################################################################
#
# Copyright (c) 2008 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

long_description = "\n\n".join((README, CHANGES))
long_description = long_description.decode('utf-8')

install_requires =[
    'setuptools',
    'pyramid',
    ]

tests_require = []

if sys.platform == "darwin":
    tests_require.append("MacFSEvents==0.1")
if sys.platform.startswith("linux"):
    tests_require.append("pyinotify==0.8.8")

tests_require = install_requires + [
    'manuel',
    'pyramid',
    ] + tests_require

setup(name='pyramid_skins',
      version = '0.3.0.2dev',
      description='Skin support for Pyramid.',
      long_description=long_description,
      keywords = "pylons pyramid",
      classifiers = [
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Zope Public License',
          'Programming Language :: Python',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Topic :: Internet :: WWW/HTTP',
          'Framework :: Pyramid'],
      license='BSD',
      packages=find_packages(),
      include_package_data = True,
      zip_safe = False,
      install_requires=install_requires,
      tests_require = tests_require,
      extras_require = {
        'tests': [dep.split('==')[0] for dep in tests_require],
          },
      test_suite="pyramid_skins.tests",
      )