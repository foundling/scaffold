#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime
import os
import sys

from tree import Tree
import utils
from validator import Validator

def main():

    BASE_PATH = os.path.abspath(os.curdir)
    SCHEMA_FILE, OUTPUT_DIR, ABS_BASE_PATH = utils.handle_args(sys.argv)
    indent_size = None


    with open(SCHEMA_FILE) as fh:
        raw_lines = fh.readlines()
        schema = utils.clean(raw_lines)

    validator = Validator()
    validator.load_schema(schema)
    validator.validate()
    indent_size = validator.get_indent_size()

    directory_tree = Tree(
        indent_size = indent_size,
        output_dir  = OUTPUT_DIR,
        base_path = BASE_PATH
    )
    directory_tree.load_data(schema)
    directory_tree.build_tree()

    def create_file(node):
        ''' File creation callback to run on each tree node. '''

        file_to_create = node['path']
        if node['children'] is None:
            open(file_to_create,'w')
        else:
            os.mkdir(file_to_create)

    directory_tree.walk(callback=create_file)

if __name__ == '__main__':
    main()
