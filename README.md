# datastore-leveldb

## datastore implementation for leveldb

See [datastore](https://github.com/datastore/datastore).
See [leveldb](https://pypi.python.org/pypi/leveldb).


### Install

From pypi (using pip):

    sudo pip install datastore.leveldb

From pypi (using setuptools):

    sudo easy_install datastore.leveldb

From source:

    git clone https://github.com/datastore/datastore.leveldb/
    cd datastore.leveldb
    sudo python setup.py install


### License

datastore.leveldb is under the MIT License.

### Contact

datastore.leveldb is written by [Juan Batiz-Benet](https://github.com/jbenet).

Project Homepage:
[https://github.com/datastore/datastore.leveldb](https://github.com/datastore/datastore.leveldb)

Feel free to contact me. But please file issues in github first. Cheers!


### Hello World

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
