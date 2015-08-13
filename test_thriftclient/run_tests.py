#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function

import sys
from os.path import dirname, exists, abspath, join

import subprocess
import nose
import logging

STDOUT = 0
STDERR = 1

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")



lavender_logger = logging.getLogger('woocheol.bulkhelper')
lavender_logger.setLevel(logging.DEBUG)

def run_all(argv=None):
    sys.exitfunc = lambda: sys.stderr.write('Shutting down...\n')

    # fetch_es_repo()

    # 항상 coverage를 넣고 테스트를 실행 한다.
    if argv is None:
        argv = [
            'nosetests', '-s', '--with-xunit',
            '--with-coverage', '--cover-package=thriftclient', '--cover-test',
        ]
    nose.run_exit(
        argv=argv,
        defaultTest=abspath(dirname(__file__))
    )


if __name__ == '__main__':
    run_all(sys.argv)
