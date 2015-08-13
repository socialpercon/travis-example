# coding: utf-8
from os.path import join
from setuptools import setup, find_packages
import sys
import os

VERSION = (0, 0, 1)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

tests_require = [
    'nose',
    'coverage'
]

# use external unittest for 2.6
if sys.version_info[:2] == (2, 6):
    tests_require.append('unittest2')

setup(
    name='thriftclient',
    description="Python thrift client for Elasticsearch",
    version=__versionstr__,
    packages=find_packages(
        where='.',
        exclude=('test_elasticsearch*', )
    ),
    classifiers=[
        "Programming Language :: Python :: 2.7"
    ],
    install_requires=install_requires,

    test_suite='test_thriftclient.run_tests.run_all',
    tests_require=tests_require,
)
