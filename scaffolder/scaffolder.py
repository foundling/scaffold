import json
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

    root = new_node(parent=None, name=OUTPUT_DIR, children=[])
    node = root
    indent = -1

    for line in schema:

        new_indent = get_indent(line, indent_size)

        # indent
        if new_indent > indent:
            if is_dir(line):
                node['children'].append( new_node(parent=node, name=get_dirname(line), children=[]) )
            else: 
                node['children'].append( new_node(parent=node, name=get_filename(line), children=None) )

            # note: first is an indent, the rest on the level aren't


            # We've come across an indent, so it's a level change. Thus:
            # append node as a child of current parent 
            # append new node to current node's children
            # have node pointer point to this new node

            

        # unindent
        elif new_indent < indent:
            # We've unindented, so we need to travel back up the tree to find the parent of the node
            # 1. Calculate difference in spaces between indent and new indent. 
            # 2. Divide by indent space.
            # 3. Call that n.
            # 4. Traverse up the tree n parents.    
            # 5. Set that node to be your new parent node.
            # 6. Append node or leaf to its children
            pass

        # no change in indentation
        else:
            if is_dir(line):
                node['children'].append( new_node(parent=node, name=get_dirname(line), children=[]) )
            else: 
                node['children'].append( new_node(parent=node, name=get_filename(line), children=None) )

            # We haven't changed levels, so:
            # 1. append whatever it is to the child array of the current node
            # 2. leave the node pointer alone

        indent = new_indent
    return root

def main():

    SCHEMA_FILE = '2test.txt'
    OUTPUT_DIR = 'test_output'

    schema_lines = open(SCHEMA_FILE).readlines()
    schema = clean(schema_lines)

    indent_size = validate_schema(schema)
    tree = build_tree(schema, indent_size, OUTPUT_DIR)
    print len(tree['children'])


if __name__ == '__main__':
    main()
