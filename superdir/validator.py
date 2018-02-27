# -*- coding: utf-8 -*-

import sys
from utils import clean, parse_indent, is_dir, is_multiple_of_indent

class Validator():


    def __init__(self, schema, output_dir=None, indent_string=None):
        ''' Bind array of cleaned schema file lines to validator object. ''' 

        self.indent_string = indent_string
        self.schema = clean(schema)
        self.output_dir = output_dir
        self.indent_size, self.start_index = self.find_first_indent()
        self.error = {'msg': None}
        self.is_valid = False

    def validate(self):

        ''' 

            Ensure absolute indent delta between current and previous line
            is no greater than 1. 

        '''

        if not len(self.schema): 
            self.error['msg'] = 'Error: empty schema file.'
            return

        prev_line = self.schema[self.start_index]
        prev_indent = self.indent_size

        lines_to_validate = self.schema[start_index + 1:]
        for index, this_line in enumerate( lines_to_validate ):

            this_indent = parse_indent(this_line, self.indent_string)
            if not self.is_valid_line(this_line, prev_line, this_indent, prev_indent):

                self.error['msg'] = 'Error in schema file on line {}'.format((index + start_index + 1))
                self.is_valid = False
                return

            prev_indent = this_indent
            prev_line = this_line

        if not self.safe_to_create(self.output_dir):
            self.error['msg'] = 'Error regarding top-level directory rules. See superdir --help for usage.'
            self.is_valid = False


    def is_valid_line(self, this_line, prev_line, cur_indent, prev_indent):
        '''
        Once the first indent size is determined, each subsequent
        indent must be:

            0 (sibling file or dir)
            equal to indent and prev line is a dir (inside a new directory)
            negative and a multiple of indent size (outside of prev directory)

        '''

        delta = cur_indent - prev_indent

        return  ( delta == 0 or
                  delta == self.indent_size and is_dir(prev_line) or
                  delta < 0 and is_multiple_of_indent(this_indent, self.indent_size) ) 

    def safe_to_create(self, output_dir):
        ''' 
            Ensure either: 
                1) an outdir exists, or
                2) schema has a single top-level dir 
        '''

        # verify get_indent_count is correct fn to use
        indents = [ get_indent_count(line, self.indent_size, self.indent_string) 
                    for line
                    in self.schema ]

        single_parent_dir = indents.count( min(indents) ) == 1 

        return bool(output_dir) or single_parent_dir

    def find_first_indent(self):
        ''' Returns indent_value and start_index of first indent. '''

        for index, line in enumerate(self.schema):
            indent_size = parse_indent(line, self.indent_string)
            if indent_size > 0:
                return indent_size, index
        else: 
            return None, None
