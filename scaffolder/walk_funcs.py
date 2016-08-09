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

def make_file_creator(base_path):

    base_path = [ base_path ]

    def _create_file(node, current_level, previous_level):

        filename = node['value']
        file_to_create = None

        if current_level > previous_level:

            # it must be a new dir, so append dir to base_path
            base_path[0] = os.path.join(base_path[0], filename) 
            file_to_create = base_path[0]

        elif current_level < previous_level:

            # it's a previous directory or file, so take differential, count down to 0, and each time, pop last path segment from base_path
            differential = previous_level - current_level
            while differential != 0:
                base_path[0] = os.path.split(base_path[0])[0]
                differential -= 1
            file_to_create = os.path.join(base_path[0], filename)

        else:
            # it's a file, so don't touch the base_path
            file_to_create = os.path.join(base_path[0], filename)

        print current_level, file_to_create

    return _create_file
