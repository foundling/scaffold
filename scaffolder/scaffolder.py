''' 
    Generates a directory tree from a reasonable, consistently-indented flat file representation. 

    Rules:
        - The indentation level must be consistent throughout the schema file. 
        - Lines that end with a '/' are directories. Everything else is a file. 
        - If a command-line argument for the root directory is not given, the schema must contain a single top-level directory.
        - If a command-line argument for the root directory is given, multiple top-level directories are allowed.
        - Blank lines (lines of length 0 after being stripped of whitespace) and comments (lines starting with '#' after being stripped of whitespace) are ignored.
        - Indentation must be preceded by a directory.

'''

def chomp(line): 
    return line[:-1]

def is_empty(line):
    return line.strip()

def is_comment(line):
    return line.lstrip().startswith('#')

def is_dir(line):
    return line.rstrip().endswith('/')

def get_indent(line):
    return len(line) - len(line.lstrip())

def get_filename(line):
    return line.strip()

def get_dirname(line):
    return line.rstrip('/')

def new_node(parent, dir_name):
    return  {
        'parent':   parent,
        'dir_name': name, 
        'children': []
    }

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

def validate_schema(schema):
    ''' Takes in a list of lines and returns indentation size if valid, throws if invalid. '''

    indent_size = 4

    return indent_size

# remove newlines and filter out empty lines
schema = [  chomp(line) 
            for line in open('test.txt').readlines() 
            if not is_empty(line) or not is_comment(line) ]

indent_size = validate_schema(schema)
indent_level = 0

root = new_node(None, 'root')
current_node = root
last_indent = indent_level

for line in schema:
    indent = get_indent(line)
    filename = get_filename(line) 

    ''' We are creating a directory, which means a new child node of the most recent directory. '''
    if indent > last_indent:

        # get last node created in current node's children, becomes parent of new dir node  
        parent = current_node['children'][-1]

        # if this line represents a directory, create a new node, append to parent's children
        if is_dir(line):
            dirname = get_dirname(line)
            new_dir_node = new_node(parent, dirname)
            parent['children'].append(new_dir_node)
        else:
            # otherwise, append its filename to parent's children
            file_name = get_filename(line)
            parent['children'].append(file_name)

        current_node = new_dir_node

    ''' We are creating a new node at the level of the parent or higher in the tree '''
    if indent < last_indent:

        # how many 'units' of indent is it less than current? call that n
        # traverse N + 1 parents 

        n = (last_indent - indent) / indent_size
        parents_to_visit = n + 1
        target_parent = find_ancestor(current_node, parents_to_visit)

        if is_dir(line):
            parent = target_parent
            dirname = get_dirname(line)
            target_parent['children'].append(parent, dirname)
        else:
            filename = get_filename(line)
            target_parent['children'].append(filename)

        # now set the current node to be target parent
        current_node = target_parent


    ''' We are just adding more dirs or files to the current node's children '''
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

    # update last_indent 
    last_indent = indent
