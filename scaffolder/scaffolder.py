''' 
    Scaffolder.py

    Generates a directory tree from a reasonable, consistently-indented flat file representation. 

    Rules:
        - The indentation level must be consistent throughout the schema file. 
        - Lines that end with a '/' are directories. Everything else is a file. 
        - If a command-line argument for the root directory is not given, the schema must contain a single top-level directory.
        - If a command-line argument for the root directory is given, multiple top-level directories are allowed.
        - Blank lines (lines of length 0 after being stripped of whitespace) and comments (lines starting with '#' after being stripped of whitespace) are ignored.
        - Indentation must be preceded by a directory.

'''

from utils import chomp, clean, is_empty, is_comment, is_dir, get_indent, parse_indent, get_filename, get_dirname, new_node, find_ancestor


def build_tree(schema, indent_size, OUTPUT_DIR):
    ''' Use indentation level of each line relative to the previous indentation level to build a tree structure. '''

    # virtual root provides a way to parse the indentation consistently.  
    virtual_root = new_node(parent=None, name='virtual_root', children=[])
    root = new_node(parent=virtual_root, name=OUTPUT_DIR, children=[])
    virtual_root['children'].append(root)
    parent_node = virtual_root

    indent = -1
    for line in schema:

        new_indent = get_indent(line, indent_size)

        if new_indent > indent:
            parent_node = parent_node['children'][-1]

        elif new_indent < indent:
            depth = indent - new_indent
            parent_node = find_ancestor(parent_node, depth)

        child = new_node(
            parent   = parent_node, 
            name     = get_dirname(line) if is_dir(line) else get_filename(line), 
            children = [] if is_dir(line) else None
        ) 
        parent_node['children'].append(child)

        indent = new_indent

    return virtual_root

def walk_tree(tree, indent, callback):

    for node in tree['children']:
        filename = node['name']
        if node['children'] is not None:
            callback(filename + '/', indent)
            walk_tree(node, indent + 4, callback)
        else:
            callback(filename, indent)

def validate_schema(schema_lines):

    ''' Validates schema and returns indent size if valid, otherwise raises ValueError.

        Once an indent size N is determined, each indentation level must be:

            1) less than N by a multiple of N,  e.g. 8 -> 4 or 8 -> 0
            2) 0, or 
            3) preceded by a directory and greater than N by exactly N.
    '''

    def less_by_factor_of_indent(this_indent, indent):
        ''' Returns True if the current indent reaches 0 when the global indent size is repeatedly subtracted from it. Otherwise returns False. '''  

        while this_indent > 0:
            this_indent -= indent

        return this_indent == 0 

    indent = None 
    start_index = 0

    # Initialize indent and line number of first indent
    for index, line in enumerate(schema_lines):
        if parse_indent(line) > 0:
            indent = parse_indent(line)
            start_index = index + 1
            break

    last_indent = indent
    for index, line in enumerate( schema_lines[start_index:] ):
        this_indent = parse_indent(line) 
        difference = this_indent - last_indent

        if (difference == 0) or (difference == indent) or (difference < 0 and less_by_factor_of_indent(this_indent, indent)):
            last_indent = this_indent
            continue
        else:
            raise ValueError('Parsing error on line {}:\n\n{}: {}'.format(index + start_index + 1, index + start_index +1, line))

    return indent


def main():

    SCHEMA_FILE = 'test.txt'
    OUTPUT_DIR = 'test_output'

    schema_lines = open(SCHEMA_FILE).readlines()
    validate_schema(schema_lines)
    schema = clean(schema_lines)

    indent_size = validate_schema(schema)
    tree = build_tree(schema, indent_size, OUTPUT_DIR)

    def print_line(line, indent_size=0):
        indented_line = indent_size * ' ' + line
        print indented_line

    walk_tree(tree, 0, callback=print_line)


if __name__ == '__main__':
    main()
