#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime
import os
import sys

import click

from tree import Tree
import utils
from validator import Validator
from walk_funcs import make_line_printer

def main():

    SCHEMA_FILE, OUTPUT_DIR = utils.handle_args(sys.argv)

    raw_lines = open(SCHEMA_FILE).readlines()
    schema = utils.clean(raw_lines)

    validator = Validator()
    validator.load_schema(schema)
    indent_size = validator.validate()

    directory_tree = Tree(

        indent_size = indent_size,
        output_dir = OUTPUT_DIR

    ).load_data(schema).build_tree()

    line_printer = make_line_printer(indent_size)
    directory_tree.walk(callback=line_printer)

if __name__ == '__main__':
    main()
