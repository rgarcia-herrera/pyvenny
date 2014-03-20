#coding: utf-8

from decimal import Decimal

def fifteen_sections(a, b, c, d):
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

             'AiBiCiD': set.intersection(a,b,c,d), }



def fifteen_normalized_sections(a, b, c, d):
    union = Decimal(len(set.union(a,b,c,d)))

    return { 'A_BuCuD': len(a - set.union(b,c,d))/union,
             'B_AuCuD': len(b - set.union(a,c,d))/union,
             'C_AuBuD': len(c - set.union(a,b,d))/union,
             'D_AuBuC': len(d - set.union(a,b,c))/union,

             'AiB_CuD': len(set.intersection(a,b) - set.union(c,d))/union,
             'AiC_BuD': len(set.intersection(a,c) - set.union(b,d))/union,
             'AiD_BuC': len(set.intersection(a,d) - set.union(b,c))/union,
             'BiC_AuD': len(set.intersection(b,c) - set.union(a,d))/union,
             'BiD_AuC': len(set.intersection(b,d) - set.union(a,c))/union,
             'CiD_AuB': len(set.intersection(c,d) - set.union(a,b))/union,

             'AiBiC_D': len(set.intersection(a,b,c) - d)/union,
             'BiCiD_A': len(set.intersection(b,c,d) - a)/union,
             'AiCiD_B': len(set.intersection(a,c,d) - b)/union,
             'AiBiD_C': len(set.intersection(a,b,d) - c)/union,

             'AiBiCiD': len(set.intersection(a,b,c,d))/union }


def render_four_set_venn( section_texts ):
    from jinja2 import Environment, FileSystemLoader

    env = Environment(loader=FileSystemLoader('templates/'))
    template = env.get_template('four_set_venn.svg')
    
    return template.render( section_texts )

