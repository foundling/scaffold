import sys

'''  
    Utility functions for scaffolder.py.  
'''

def usage(out=sys.stdout):
    out.write('Usage: scaffolder SCHEMA_FILE [TARGET]')

def clean(lines):
    return [ line.strip() for line in lines if not is_empty(line) and not is_comment(line) ] 

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

