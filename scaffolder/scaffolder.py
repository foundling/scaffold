import pdb

from utils import chomp, clean, is_empty, is_comment, is_dir, get_indent, get_filename, get_dirname, new_node,  find_ancestor, validate_schema, walk_tree

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

def build_tree(schema, indent_size, OUTPUT_DIR):
    ''' use the indentation level on each line relative to the previous indentation level to build a tree structure. '''

    indent = -1

    # virtual root provides a way to parse the indentation consistently.  
    virtual_root = new_node(parent=None, name='virtual_root', children=[])
    root = new_node(parent=virtual_root, name=OUTPUT_DIR, children=[])
    virtual_root['children'].append(root)

    parent_node = virtual_root

    for line in schema:

        new_indent = get_indent(line, indent_size)

        if new_indent > indent:
            parent_node = parent_node['children'][-1]

        elif new_indent < indent:
            depth = indent - new_indent
            parent_node = find_ancestor(parent_node, depth)

        if is_dir(line):
            parent_node['children'].append( new_node(parent=parent_node, name=get_dirname(line), children=[]) )
        else: 
            parent_node['children'].append( new_node(parent=parent_node, name=get_filename(line), children=None) )

        indent = new_indent

    return virtual_root

def walk_tree(tree, indent):
    for node in tree['children']:
        if node['children'] is not None:
            print ''.join([indent * ' ', node['name'] + '/'])
            walk_tree(node, indent + 4)
        else:
            print ''.join([indent * ' ', node['name']])

def main():

    SCHEMA_FILE = 'test.txt'
    OUTPUT_DIR = 'test_output'

    schema_lines = open(SCHEMA_FILE).readlines()
    schema = clean(schema_lines)

    indent_size = validate_schema(schema)
    tree = build_tree(schema, indent_size, OUTPUT_DIR)
    walk_tree(tree, 0)


if __name__ == '__main__':
    main()

'''

dir1/
app/
    file1.txt
    dir2/
#    app/
#    README.txt
#    LICENSE.txt
#    docs/
#    test/

'''
