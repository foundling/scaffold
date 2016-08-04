'''  Utility functions for scaffolder.py.  '''

def usage():
    print '''
    Usage: scaffolder SCHEMA_FILE [TARGET]
    '''

def print_line(line, indent_size):
    indented_line = indent_size * ' ' + line
    print indented_line

def clean(lines):
    return [ chomp(line) for line in lines if not is_empty(line) and not is_comment(line) ] 

def chomp(line):
    return line[:-1]

def is_empty(line):
    return line.strip() is ''

def is_comment(line):
    return chomp(line).lstrip().startswith('#')

def is_dir(line):
    return line.rstrip().endswith('/')

def is_multiple_of_indent(this_indent, indent):
    ''' Returns True if the current indent reaches 0 when the global indent size is repeatedly subtracted from it. Otherwise returns False. '''

    while this_indent > 0:
        this_indent -= indent

    return this_indent == 0

def parse_indent(line):
    ''' Return the leading number of spaces in a line of text. '''
    return len(line) - len(line.lstrip())

def get_indent(line, indent_size):
    ''' Return the number of indentation units after dividing a line of text's leading space count by some indent_size. '''
    raw_indent = len(line) - len(line.lstrip())

    rv = None 

    try:
        rv = raw_indent / indent_size

    except ZeroDivisionError:
        rv = 0

    return rv
            
def get_filename(line):
    return line.strip()

def get_dirname(line):
    return line.strip().rstrip('/')

def new_node(parent=None, name=None, children=None):
    return  dict(parent=parent, name=name, children=children)

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
