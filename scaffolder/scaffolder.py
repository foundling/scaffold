#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime
import os
import sys

import click

from tree import Tree
import utils
import validator



''' 
    scaffolder.py

    generates a directory tree from a reasonable, consistently-indented flat file representation of a file system. 

    here's an example:

    scaffolder/
        scaffolder/
            scaffolder.py
            validator.py
            tree.py
            test/
                scaffolder_test.py
                validator_test.py
                tree_test.py
            readme.md
            license.md
        test/
        docs/
        readme.md
        license.md

    rules:
        - the indentation level must be consistent throughout the schema file. 
        - lines that end with a '/' are directories. everything else is a file. 
        - if a command-line argument for the root directory is not given, the schema must contain a 
        single top-level directory.
        - if a command-line argument for the root directory is given, multiple top-level directories 
        are allowed.
        - blank lines (lines of length 0 after being stripped of whitespace) and comments (lines starting with 
        '#' after
        being stripped of whitespace) are ignored.
        - indentation must be preceded by a directory.

'''

def handle_args(*args):

    #
    #  Provisional argument handling to be replaced by click.
    #
    #  Usage: scaffolder SCHEMA [OUTPUT_DIR]
    #
    
    schema_file = None
    output_dir = None

    if len(args) < 2:
        utils.usage()
        sys.exit(1)

    if len(args) == 2:
        schema_file = args[1] 

        dt_now = datetime.datetime.now()
        date_string = str(dt_now) 
        date_label = datestring.split(' ')[0]
        output_dir = 'SCAFFOLD_OUTPUT_{}'.format(date_label)

    if len(args) > 2:

        if os.path.isdir(args[2]):
            print ("An error has occurred: the output directory '{}' exists. In order to run scaffolder successfully, \n"
            "either rename your output directory or rename the currently directory with the name you've supplied.").format(output_dir)
            utils.usage()
            sys.exit(1) 

        else:
            schema_file = args[]
            output_dir = args[]   


def main():

    SCHEMA_FILE, OUTPUT_DIR = handle_args(sys.argv)

    schema_lines = open(SCHEMA_FILE).readlines()
    indent_size = validator.validate_schema(schema_lines)
    schema = utils.clean(schema_lines)

    directory_tree = Tree(
        input=schema,
        indent_size=indent_size,
        output_dir=OUTPUT_DIR
    )
    directory_tree.build_tree()

    def make_line_printer(indent, indent_char=' '):

        def _print_line(node):
            ''' The contract with directory_tree: args are a dict with parent, children and value properties. '''

            line = node['name']
            if node['children'] is not None:
                line += '/'

            print (indent * indent_char) + line

        return _print_line

    line_printer = make_line_printer(indent_size)
    directory_tree.walk(callback=line_printer)

if __name__ == '__main__':
    main()
