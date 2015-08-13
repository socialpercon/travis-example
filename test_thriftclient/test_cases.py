from thriftclient.bulkhelper import BulkHelper
from os.path import dirname, join
import json

try:
    # python 2.6
    import unittest2 as unittest
except ImportError:
    import unittest


class TestBulkHelper(unittest.TestCase):
    def test_start(self):
        bulk = BulkHelper()
        result = bulk.run()
        self.assertEquals('bulk', result)


if __name__ == '__main__':
    unittest.main()
