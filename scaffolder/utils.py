import datetime

import os
import sys


'''  
    Utility functions for scaffolder.py.  
'''

def usage(out=sys.stdout):
    out.write('Usage: scaffolder SCHEMA_FILE [TARGET]\n')

def clean(lines):
    return [ line.rstrip() for line in lines if not is_empty(line) and not is_comment(line) ] 

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

def handle_args(args):

    #
    #  Provisional argument handling to be replaced by click.
    #
    #  Usage: scaffolder SCHEMA [OUTPUT_DIR]
    #
    
    schema_file = None
    output_dir = None

    if len(args) < 2:
        usage()
        sys.exit(1)

    if len(args) == 2:
        schema_file = args[1] 

        dt_now = datetime.datetime.now()
        date_string = str(dt_now) 
        date_label = date_string.split(' ')[0]
        output_dir = 'SCAFFOLDER_OUTPUT_{}'.format(date_label)

    if len(args) > 2:

        if os.path.isdir(args[2]):
            print ("An error has occurred: the output directory '{}' exists. In order to run scaffolder successfully, \n"
            "either rename your output directory or rename the currently directory with the name you've supplied.").format(output_dir)
            usage()
            sys.exit(1) 

        else:
            schema_file = args[1]
            output_dir = args[2]   

    return schema_file, output_dir
