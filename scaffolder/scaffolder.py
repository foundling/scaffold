''' Generates a directory tree from a reasonable, consistently indented flat-file representation. '''

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
    ''' Use relative dedent level to determine parent.
        1 dedent -> append new node to parent's parent's child node  
        N is a unit of dedent, then we travel up N + 1 parents and append a new node to its children
    '''
    pass

def validate_schema(schema):
    ''' Takes in a list of lines and returns indentation level and value if valid, throws if invalid. '''

    indent_level = 0 
    indent_size = 4

    return indent_level, indent_size

schema = [  chomp(line) 
            for line in open('test.txt').readlines() 
            if line.strip() ]
indent_level, indent_size = validate_schema(schema)
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
