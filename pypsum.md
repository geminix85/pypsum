# About pypsum.py #
pypsum.py is a command line tool or a python module, whatever you want it to be.
### Running pypsum.py from the command line ###
You can run pypsum.py from the command line. It has a few options:
```
$ ./pypsum.py --help
Usage: pypsum.py [options]

Options:
  -h, --help            show this help message and exit
  -n X, --howmany=X     how many items to get
  -w TYPE, --what=TYPE  the type of items to get: paras, words, bytes, lists
  -l, --start-with-Lorem
                        Start the text with "Lorem ipsum"
```
Here's a usage example:
```
$ ./pypsum.py --howmany=20 -w words -l
Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Sed nulla erat, porta sit amet, sagittis eget, semper et, nunc. Cras.

Generated 1 paragraph, 20 words, 127 bytes of Lorem Ipsum
```

### pypsum.py as Python module ###
pypsum.py is a python module which you can import into your own program and provides one function: get\_lipsum. Useful stuff:
```
>>> import pypsum
>>> print pypsum.get_lipsum.__doc__
Get lorem ipsum text from lipsum.com. Parameters:
howmany: how many items to get
what: the type of the items [paras/words/bytes/lists]
start_with_lipsum: whether or not you want the returned text to start with Lorem ipsum [yes/no]
Returns a tuple with the generated text on the 0 index and generation statistics on index 1
```