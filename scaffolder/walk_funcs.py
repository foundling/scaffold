import os

''' 
    walk_funcs.py

    Functions to run on each node in the tree. 
'''

def make_line_printer(indent, indent_char=' '):
    ''' Make a function that prints out each node as a file or directory and indents accordingly. '''

    def _print_line(node, level=0):

        line = node['value']
        if node['children'] is not None:
            line += '/'

        print (indent_char * level * indent) + line

    return _print_line

def make_file_creator(base_dir):
    ''' approach: write files from a single location using stack.  '''

    def file_creator(node):

        filename = node['value']
        children = node['children']

        if children is None:
            if not os.path.exists(filename):
                try:
                    open(filename,'w')
                except IOError:
                    print "IO ERROR when attempting to write the file '{}' to the directory {}.".format(filename, cur_dir)
        else:
            try:
                os.mkdir(filename)
            except IOError:
                print "IO ERROR when attempting to create directory '{}' to the directory {}.".format(filename, cur_dir)
