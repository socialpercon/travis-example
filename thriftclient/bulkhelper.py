# coding: utf-8

from threading import Timer
from Queue import Queue, Empty

import logging
import traceback

# Globals
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('woocheol.bulkhelper')


class BulkHelper(object):
    def __init__(self):
        self._timer = None

    def run(self):
        return 'bulk'


def main():
    pass


if __name__ == '__main__':
    main()
