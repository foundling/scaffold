''' 
    Generates a directory tree from a reasonable, consistently indented flat-file representation. 

    Rules:
        - Indentation must be consistent 
        - First Line must contain no indentation
        - Comments must start with '#'

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

def is_empty(line):
    return line.strip()

def is_comment(line):
    return line.lstrip().startswith('#')

def get_indent(line):
    return len(line) - len(line.lstrip())

def get_filename(line):
    return line.strip()

def get_dirname(line):
    return line.rstrip('/')


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

# remove newlines and filter out empty lines
schema = [  chomp(line) 
            for line in open('test.txt').readlines() 
            if not is_empty(line) or not is_comment(line) ]

indent_level, indent_size = validate_schema(schema)
root = new_node(None, 'root')

current_node = root
last_indent = indent_level

for line in schema:
    indent = get_indent(line)
    filename = get_filename(line) 
    is_dir = filename.rstrip().endswith('/')

    if indent > last_indent:
        ''' We are creating a new node lower in the tree. '''

        # get last child in current node's children 
        node = current_node.children[-1]

    if indent < last_indent:
        ''' We are creating a new node higher up or at the same level in the tree '''
        print 'parent or sibling'

    else:
        print ''' adding children to current node '''
        if is_dir:
            parent = current_node['parent']
            dirname = get_dirname(line)
            new_dir_node = new_node(parent, dirname)
            current_node['children'].append(new_dir_node)
        else:
            filename = get_filename(line)
            current_node['children'].append(filename) 

    ''' update last_indent ''' 
    last_indent = indent
