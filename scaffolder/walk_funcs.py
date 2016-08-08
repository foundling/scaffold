''' 
    walk_funcs.py 

    Functions to run on each node in the tree. 

'''
def make_line_printer(indent, indent_char=' '):
    ''' make a function that prints out each node as a file or directory and indents accordingly '''

    def _print_line(node):

        line = node['name']
        if node['children'] is not None:
            line += '/'

        print (indent * indent_char) + line

    return _print_line


