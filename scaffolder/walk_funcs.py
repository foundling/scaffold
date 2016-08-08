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


