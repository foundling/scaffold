import sys
import os
import re


def get_indent(lines):
    '''
        Get the indentation level of the file. Default is 0. 
    '''

    indent_found = False 
    indent = 0

    for line in lines:
        leading_spaces = len(line) - len(line.lstrip())
        if leading_spaces and not indent_found:
            indent_found = True
            indent = leading_spaces
            break

    return indent

def validate_schema(lines, indent):
    '''
        Take a list of lines and compare their indent against the indent arg.
        Comparison is only made if leading_spaces is not 0.
    '''

    for line in lines:
        leading_spaces = len(line) - len(line.lstrip())
        print leading_spaces
        if leading_spaces and leading_spaces != indent:
            raise ValueError('Indentation does not match inital indent of\
                              {} spaces'.format(indent))

    print ''.join(lines)
    return True

def err(msg):
    ''' 
        print out an error message and exit with status 1. 
    '''
    print msg
    sys.exit(1)

def main():

    f, output_path = sys.argv[1:3]
    lines = open(f).readlines()
    output_dir = os.mkdir(output_path)

    indent_count = get_indent(lines)
    is_valid = validate_schema(lines, indent_count)

if __name__ == '__main__':
    main()
