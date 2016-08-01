''' 
    Scaffolder.py
    Use a flat-file with consistent indentation to create a directory tree 
'''

from scaffolder import new_node

def new_node(parent, dir_name):
    return  {
        'parent':   parent,
        'dir_name': name, 
        'children': []
    }

def chomp(line): 
    return line[:-1]

def get_indent(line):
    return len(line) - len(line.lstrip())

def find_ancestor(parent_count):
    ''' 
        Use relative dedent level to determine parent.
        1 dedent -> append new node to parent's parent's child node  
        N is a unit of dedent, then we travel up N + 1 parents and append a new node to its children
    '''

    pass

indent_level = 0 
indent_value = 4
schema = [  chomp(line) 
            for line in open('test.txt').readlines() 
            if line.strip() ]
root = new_node(None, 'root')
current_node = root

for line in schema:
    indent = get_indent(line)
    is_dir = line.rstrip().endswith('/')

    if indent > last_indent:
        ''' We are creating a new node lower in the tree ''' 
        ''' Must be a directory that triggers this '''

        ''' get last child in current node's children '''
        node = current_node.children[-1]

    if indent < last_indent:
        ''' We are creating a new node higher up or at the same level in the tree '''
        print 'parent or sibling'

    else:
        print ''' adding children to current node '''

    ''' update last_indent ''' 
    last_indent = indent
