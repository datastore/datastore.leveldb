
__version__ = '0.0.1'
__author__ = 'Juan Batiz-Benet'
__email__ = 'juan@benet.ai'
__doc__ = '''
leveldb datastore implementation.

Tested with:
  * datastore 0.3.0
  * pyleveldb 0.19

'''

import leveldb
import datastore.core


class LevelDBDatastore(datastore.Datastore):
  '''LevelDB datastore. Does not support queries yet.


  Hello World:

      >>> import datastore.leveldb
      >>>
      >>> ds = datastore.leveldb.LevelDBDatastore('./db')
      >>>
      >>> hello = datastore.Key('hello')
      >>> ds.put(hello, 'world')
      >>> ds.contains(hello)
      True
      >>> ds.get(hello)
      'world'
      >>> ds.delete(hello)
      >>> ds.get(hello)
      None

  '''

  def __init__(self, dbpath):
    '''Initialize leveldb with given `dbpath`.

    Args:
      dbpath: A file path for leveldb to use.
    '''
    self.leveldb = leveldb.LevelDB(dbpath)


  def get(self, key):
    '''Return the object in leveldb named by `key` or None.

    Args:
      key: Key naming the object to retrieve.

    Returns:
      object or None
    '''
    try:
      return self.leveldb.Get(str(key))
    except KeyError:
      return None


  def put(self, key, value):
    '''Stores the object `value` named by `key` in leveldb.

    Args:
      key: Key naming `value`.
      value: the object to store.
    '''
    self.leveldb.Put(str(key), value)


  def delete(self, key):
    '''Removes the object named by `key` in leveldb.

    Args:
      key: Key naming the object to remove.
    '''
    self.leveldb.Delete(str(key))
