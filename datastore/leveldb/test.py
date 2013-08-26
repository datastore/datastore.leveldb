
import os
import shutil
import unittest

import datastore.core
from datastore import serialize
from datastore.core.test.test_basic import TestDatastore

from . import LevelDBDatastore


class TestLevelDBDatastore(TestDatastore):

  tmp = os.path.normpath('/tmp/datastore.test.leveldb')

  def setUp(self):
    if os.path.exists(self.tmp):
      shutil.rmtree(self.tmp)
    os.mkdir(self.tmp)

  def tearDown(self):
    shutil.rmtree(self.tmp)

  def test_leveldb(self):
    dirs = map(str, range(0, 4))
    dirs = map(lambda d: os.path.join(self.tmp, d), dirs)
    ldss = map(LevelDBDatastore, dirs)
    dses = map(serialize.shim, ldss)
    self.subtest_simple(dses, numelems=500)


if __name__ == '__main__':
  unittest.main()
