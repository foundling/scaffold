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
