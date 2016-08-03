
''' Utility functions for scaffolder.py '''

def chomp(line):
    return line[:-1]

def is_empty(line):
    return line.strip() is ''

def is_comment(line):
    return chomp(line).lstrip().startswith('#')

def is_dir(line):
    return line.rstrip().endswith('/')

def parse_indent(line):
    ''' Return the leading number of spaces in a line of text. '''
    return len(line) - len(line.lstrip())

def get_indent(line, indent_size):
    ''' Return the number of indentation units after dividing a line of text's leading space count by some indent_size. '''
    raw_indent = len(line) - len(line.lstrip())
    return raw_indent / indent_size

def get_filename(line):
    return line.strip()

def get_dirname(line):
    return line.strip().rstrip('/')

def new_node(parent=None, name=None, children=None):
    return  dict(parent=parent, name=name, children=children)

def clean(lines):
    return [ chomp(line) for line in lines if not is_empty(line) and not is_comment(line) ] 


def find_ancestor(start_node, parents_to_visit):
    ''' Use relative dedent level to determine parent.
        1 dedent -> append new node to parent's parent's child node  
        N is a unit of dedent, then we travel up N + 1 parents and append a new node to its children
    '''
    current_node = start_node

    while (parents_to_visit > 0):
        current_node = current_node['parent']
        parents_to_visit -= 1

    return current_node
