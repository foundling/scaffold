# -*- coding: utf-8 -*-

'''  
    Utility functions for superdir.py.  
'''

from __future__ import print_function 
import datetime

import os
import sys

def is_empty(line):
    return line.strip() is ''

def is_comment(line):
    return line.strip().startswith('#')

def is_dir(line):
    return line.rstrip().endswith('/')

def is_multiple_of_indent(this_indent, global_indent):
    ''' Returns True if the current indent reaches 0 when the global indent size is repeatedly subtracted from it. Otherwise returns False. '''

    while this_indent > 0:
        this_indent -= global_indent

    return this_indent == 0

def clean(lines):
    ''' discard all comments and lines with nothing or whitespace ''' 

    return [ 
            line.rstrip() 
            for line in lines 
            if not ( is_empty(line) or is_comment(line) ) ]

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
            
def get_dirname(line):
    ''' Remove all trailing forward slashes from a line after it's been stripped. '''

    return line.strip().rstrip('/')

def get_filename(line):
    ''' return line with whitespace stripped. '''

    return line.strip()

def get_paths(output_dir):
    ''' Takes the output directory and breaks it into the relative directory name and the base path/starting point for the traversal 

    ABSOLUTE:

        original output_dir = /data/apps/new_app 

        output_dir = new_app 
        full_base_path = /data/apps

    RELATIVE WITH MULTIPLE LEVELS:

        original output_dir = apps/new_app 

        output_dir = new_app 
        full_base_path = cwd() + '/' + apps/

    RELATIVE WITH A SINGLE LEVEL:

        original_output_dir = new_app

        output_dir = new_app 
        full_base_path = cwd() 

    '''

    abs_cur_dir = os.path.abspath(os.curdir)
    full_base_path = None

    # absolute path example: /data/apps/new_app
    if output_dir.startswith('/'):
        abs_base_path = os.path.join('/', *output_dir.split('/')[:-1])
        output_dir = output_dir.split('/')[-1]

    # relative path with multiple dirs example: apps/new_app 
    else:
        if '/' in output_dir:
            abs_base_path = os.path.join( abs_cur_dir, '/'.join(output_dir.split('/')[:-1]) )
            output_dir = output_dir.split('/')[-1]
        else:
            abs_base_path = abs_cur_dir 

    return output_dir, abs_base_path

def usage(out=sys.stdout):
    ''' Print usage info. '''

    out.write('Usage: superdir SCHEMA_FILE [TARGET]\n')

def show_err_msg(out=sys.stdout, line_number=None, schema_lines=None):
    ''' Print an error message including the line number and the line. ''' 

    schema_lines[line_number] = schema_lines[line_number].rstrip() + '    <<< error'
    highlighted_schema = '\n'.join(schema_lines)
    out.write('Parse Error: inconsistent indentation in your schema file on line {}\n{}\n'.format(line_number, highlighted_schema))
