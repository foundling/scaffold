#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime
import os
import sys

import click

from tree import Tree
import utils
import validator
import walk_funcs


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


def main():

    SCHEMA_FILE, OUTPUT_DIR = utils.handle_args(sys.argv)

    raw_lines = open(SCHEMA_FILE).readlines()
    schema = utils.clean(raw_lines)
    indent_size = validator.validate_schema(schema)

    directory_tree = Tree(

        input=schema,
        indent_size=indent_size,
        output_dir=OUTPUT_DIR

    ).build_tree()

    line_printer = walk_funcs.make_line_printer(indent_size)
    directory_tree.walk(callback=line_printer)

if __name__ == '__main__':
    main()
