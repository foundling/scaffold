#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' 
    Scaffolder.py

    Generates a directory tree from a reasonable, consistently-indented flat file representation. 

    Rules:
        - The indentation level must be consistent throughout the schema file. 
        - Lines that end with a '/' are directories. Everything else is a file. 
        - If a command-line argument for the root directory is not given, the schema must contain a single top-level directory.
        - If a command-line argument for the root directory is given, multiple top-level directories are allowed.
        - Blank lines (lines of length 0 after being stripped of whitespace) and comments (lines starting with '#' after being stripped of whitespace) are ignored.
        - Indentation must be preceded by a directory.

'''

import os
import sys

import click

import utils
import tree
import validator

def main():

    # provisional argument handling to be replaced by click
    if len(sys.argv) < 2:
        utils.usage()
        sys.exit(1)

    if len(sys.argv) == 2:
        SCHEMA_FILE = sys.argv[1] 
        OUTPUT_DIR = 'output_dir'

    if len(sys.argv) >= 3:

        if os.path.isdir(sys.argv[2]):
            print ("The output directory '{}' exists. In order to run scaffolder successfully, \n"
                    "either rename your output directory or rename the currently existing directory.").format(OUTPUT_DIR)
            sys.exit(1) 
        else:
            SCHEMA_FILE = sys.argv[1]
            OUTPUT_DIR = sys.argv[2]


    schema_lines = open(SCHEMA_FILE).readlines()
    indent_size = validator.validate_schema(schema_lines)
    schema = utils.clean(schema_lines)

    dir_tree = tree.build_tree(schema, indent_size, OUTPUT_DIR)

    tree.walk_tree(dir_tree, 0, callback=utils.print_line)


if __name__ == '__main__':
    main()
