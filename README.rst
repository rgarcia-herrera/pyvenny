pyvenny
=======

Plot four set venn diagrams, like venny (http://bioinfogp.cnb.csic.es/tools/venny/)
but using python sets:

Installation
------------

Install library, perhaps within a virtualenv::

    $ pip install pyvenny


Command line interface
----------------------

A command line script is included, vennyplot::

    usage: vennyplot [-h] --output OUTPUT --sets SETS SETS SETS SETS
                     [--labels LABELS LABELS LABELS LABELS]
    
    Generate a Venn diagram of four files taken as sets of lines.
    
    optional arguments:
      -h, --help            show this help message and exit
      --output OUTPUT       absolute path to output file
      --sets SETS SETS SETS SETS
                            absolute paths to four files
      --labels LABELS LABELS LABELS LABELS
                            four set labels
    
    
Aplication Programming Interface
--------------------------------

Use it within your Python code::

    >>> import pyvenny
    >>> with open('diagram.svg', 'w') as f:
             f.write( pyvenny.render_four_set_venn(
             set(['a','b','c','d']),
             set(['b','c','d','e']),
             set(['c','d','e','f']),
             set(['d','e','f','g']))
