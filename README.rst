pyvenny
=======

Plot four set venn diagrams, like venny (http://bioinfogp.cnb.csic.es/tools/venny/)
but using python sets:

I just drew the damn thing using inkscape and then used that as a jinja template.
Set algebra I just did by hand.

To use:

    >>> import pyvenny
    >>> with open('diagram.svg', 'w') as f:
             f.write( pyvenny.render_four_set_venn(
             set(['a','b','c','d']),
             set(['b','c','d','e']),
             set(['c','d','e','f']),
             set(['d','e','f','g']))
