# -* coding: utf-8 -*-

import sys
from utils import clean, parse_indent, is_dir, is_sibling, is_parent, is_child, get_indent_count

class Validator():

    def __init__(self, schema, output_dir=None, indent_string=None):
        ''' Bind array of cleaned schema file lines to validator object. ''' 

        self.indent_string = indent_string
        self.schema = clean(schema)
        self.output_dir = output_dir
        self.indent_size, self.start_index = self.find_first_indent()
        self.error = None
        self.is_valid = True

    def validate(self):
        ''' 
            Scan schema file line by line comparing new line to previous line.
            Finally, make sure schema conforms to directory creation rules.
        '''

        if not len(self.schema): 
            self.error = 'Error: empty schema file.'
            return

        lines_to_validate = self.schema[self.start_index + 1:]
        prev_line, prev_indent = self.schema[self.start_index], self.indent_size

        for index, cur_line in enumerate(lines_to_validate):

            cur_indent = parse_indent(cur_line, self.indent_string)
            if not self.is_valid_line(prev_line, cur_indent, prev_indent):

                current_line = index + self.start_index + 1
                self.error = 'Error in schema file on line {}'.format(current_line)
                self.is_valid = False
                return

            prev_indent = cur_indent
            prev_line = cur_line

        if not self.safe_to_create(self.output_dir):
            self.error = 'Error regarding top-level directory rules. See superdir --help for usage.'
            self.is_valid = False


    def is_valid_line(self, prev_line, cur_indent, prev_indent):
        '''
        Once the first indent size is determined, each subsequent relative 
        indent must be:

            - 0: current line represents a sibling file or directory
            - equal to indent and prev line is a dir: current line represents a 
            nested directory)
            - negative and a multiple of indent size: line represents a directory
            higher up in the file tree.

        '''

        delta = cur_indent - prev_indent

        return  ( is_sibling(delta) or 
                  is_child(delta, self.indent_size, prev_line) or 
                  is_parent(delta, self.indent_size, cur_indent) ) 

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
        ''' Returns indent_size, start_index of first indent. '''

        for index, line in enumerate(self.schema):
            indent_size = parse_indent(line, self.indent_string)
            if indent_size > 0:
                return indent_size, index
        else: 
            return None
