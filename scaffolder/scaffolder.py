import json
import pdb

from utils import chomp, is_empty, is_comment, is_dir, get_indent, get_filename, get_dirname, new_node, find_ancestor, validate_schema, walk_tree

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

def build_tree(schema, indent_size):

    root = new_node(None, 'root')
    current_node = root
    last_indent = -1 * indent_size

    #pdb.set_trace()
    for line in schema:

        new_indent = get_indent(line)

        if new_indent > last_indent:

            parent = current_node['children'][-1]

            if is_dir(line):
                dirname = get_dirname(line)
                new_dir_node = new_node(parent, dirname)
                parent['children'].append(new_dir_node)
                current_node = new_dir_node

                last_indent = new_indent

            else:
                filename = get_filename(line)
                parent['children'].append(filename)


        elif new_indent < last_indent:

            n = (last_indent - new_indent) / indent_size
            parents_to_visit = n + 1
            target_parent = find_ancestor(current_node, parents_to_visit)

            if is_dir(line):
                parent = target_parent
                dirname = get_dirname(line)
                target_parent['children'].append(parent, dirname)

            else:
                filename = get_filename(line)
                target_parent['children'].append(filename)

            current_node = target_parent

        else:

            if is_dir(line):
                parent = current_node['parent'] # if indentation is 0, parent is null, which is WRONG 
                dirname = get_dirname(line)
                new_dir_node = new_node(parent, dirname)
                current_node['children'].append(new_dir_node)

            else:
                filename = get_filename(line)
                leaf = new_leaf()
                current_node['children'].append() 


    return root

def main():

    schema_file = '2test.txt'
    schema = [  chomp(line) 
                for line in open(schema_file).readlines() 
                if not is_empty(line) or not is_comment(line) ]

    indent_size = validate_schema(schema)
    tree = build_tree(schema, indent_size)
    print tree

if __name__ == '__main__':
    main()
