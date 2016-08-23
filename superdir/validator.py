# -*- coding: utf-8 -*-

from __future__ import print_function 
import sys
from utils import get_indent, parse_indent, is_empty, is_comment, is_dir,\
                  is_multiple_of_indent, clean, show_err_msg,\
                  build_output_dirname 

class Validator():

    def __init__(self, output_dir=None):

        self.indent = None
        self.schema = None
        self.indent_size = None
        self.output_dir = output_dir

    def load_schema(self, schema):

        self.schema = clean(schema)

    def validate_indent(self):
        ''' 
        Validates schema and raises ValueError if invalid.

        Once the first indent size is determined, each subsequent
        indent must be:

            1) less than N by a multiple of N,  e.g. 8 -> 4 or 8 -> 0
            2) 0, or 
            3) preceded by a directory and greater than N by exactly N.
        '''

        indent, start_index = self._find_first_indent()

        prev_indent = indent
        prev_line = self.schema[start_index]
        for index, line in enumerate( self.schema[start_index + 1:] ):

            this_indent = parse_indent(line) 
            difference = this_indent - prev_indent
            valid_line = ( 
                (difference == 0) or\
                (difference == indent and is_dir(prev_line)) or\
                (difference < 0 and is_multiple_of_indent(this_indent, indent))             ) 

            if not valid_line:
                show_err_msg(
                    line_number = (index + start_index + 1),
                    schema_lines = self.schema[:]
                )
                raise SystemExit(1) 

            prev_indent = this_indent
            prev_line = line
            continue

        self.check_top_dir(self.output_dir)
        self.indent_size = indent

    def check_top_dir(self, output_dir):

        indents = [ parse_indent(line) for line in self.schema ]
        min_indent = min(indents) 
        default_dirname = None 

        if indents.count(min_indent) > 1 and not output_dir:

            sys.stdout.write('''Parse Error: You have multiple top-level 
                                directories but you have not supplied an output                                directory. See superdir --help for more 
                                information''')
            raise SystemExit(1)

    def get_indent_size(self):

        return self.indent_size

    def _find_first_indent(self):
        ''' Returns indent_value, start_index of first indent. '''

        indent, start_index = 0, 0 

        for index, line in enumerate(self.schema):
            if parse_indent(line) > 0:
                indent = parse_indent(line)
                break

        return indent, start_index
