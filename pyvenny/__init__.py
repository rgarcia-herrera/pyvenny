#coding: utf-8

from decimal import Decimal
from jinja2 import Environment, PackageLoader
    

def fifteen_normalized_sections(a, b, c, d):
    union = Decimal(len(set.union(a,b,c,d)))

    # get sizes for regions delimited by set areas
    # _ is for - as in substract, i is for intersection, u is for union
    return { 'A_BuCuD': "%0.2f" % (len(a - set.union(b,c,d))/union),
             'B_AuCuD': "%0.2f" % (len(b - set.union(a,c,d))/union),
             'C_AuBuD': "%0.2f" % (len(c - set.union(a,b,d))/union),
             'D_AuBuC': "%0.2f" % (len(d - set.union(a,b,c))/union),

             'AiB_CuD': "%0.2f" % (len(set.intersection(a,b) - set.union(c,d))/union),
             'AiC_BuD': "%0.2f" % (len(set.intersection(a,c) - set.union(b,d))/union),
             'AiD_BuC': "%0.2f" % (len(set.intersection(a,d) - set.union(b,c))/union),
             'BiC_AuD': "%0.2f" % (len(set.intersection(b,c) - set.union(a,d))/union),
             'BiD_AuC': "%0.2f" % (len(set.intersection(b,d) - set.union(a,c))/union),
             'CiD_AuB': "%0.2f" % (len(set.intersection(c,d) - set.union(a,b))/union),

             'AiBiC_D': "%0.2f" % (len(set.intersection(a,b,c) - d)/union),
             'BiCiD_A': "%0.2f" % (len(set.intersection(b,c,d) - a)/union),
             'AiCiD_B': "%0.2f" % (len(set.intersection(a,c,d) - b)/union),
             'AiBiD_C': "%0.2f" % (len(set.intersection(a,b,d) - c)/union),

             'AiBiCiD': "%0.2f" % (len(set.intersection(a,b,c,d))/union) }



def fifteen_subsets(a, b, c, d):
    union = Decimal(len(set.union(a,b,c,d)))

    # get sizes for regions delimited by set areas
    # _ is for - as in substract, i is for intersection, u is for union
    return { 'A_BuCuD': a - set.union(b,c,d),
             'B_AuCuD': b - set.union(a,c,d),
             'C_AuBuD': c - set.union(a,b,d),
             'D_AuBuC': d - set.union(a,b,c),

             'AiB_CuD': set.intersection(a,b) - set.union(c,d),
             'AiC_BuD': set.intersection(a,c) - set.union(b,d),
             'AiD_BuC': set.intersection(a,d) - set.union(b,c),
             'BiC_AuD': set.intersection(b,c) - set.union(a,d),
             'BiD_AuC': set.intersection(b,d) - set.union(a,c),
             'CiD_AuB': set.intersection(c,d) - set.union(a,b),

             'AiBiC_D': set.intersection(a,b,c) - d,
             'BiCiD_A': set.intersection(b,c,d) - a,
             'AiCiD_B': set.intersection(a,c,d) - b,
             'AiBiD_C': set.intersection(a,b,d) - c,

             'AiBiCiD': set.intersection(a,b,c,d)}

             

def render_four_set_venn( a, b, c, d, titles={'A': 'A',
                                              'B': 'B',
                                              'C': 'C',
                                              'D': 'D'} ):
    sections = fifteen_normalized_sections( a, b, c, d )
                          
    env = Environment(loader=PackageLoader('pyvenny', 'templates'))
    template = env.get_template('four_set_venn.svg')
    
    return template.render( dict(sections.items() + titles.items()) )

