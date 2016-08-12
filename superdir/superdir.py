#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import datetime
import os
import sys

from tree import Tree
import utils
from validator import Validator
from args_handler import handle_args 

def create_file(node):
    ''' File creation callback to run on each tree node. '''

    file_to_create = node['path']
    if node['children'] is None:
        open(file_to_create,'w')
    else:
        os.mkdir(file_to_create)


def main():

    BASE_PATH = os.path.abspath(os.curdir)
    schema, OUTPUT_DIR = handle_args(sys.argv[1:])
    indent_size = None

    validator = Validator()
    validator.load_schema(schema)
    validator.validate()
    indent_size = validator.get_indent_size()

    directory_tree = Tree(
        indent_size = indent_size,
        output_dir  = OUTPUT_DIR,
        base_path   = BASE_PATH
    )
    directory_tree.load_data(schema)
    directory_tree.build_tree()
    directory_tree.walk(callback=create_file)

if __name__ == '__main__':
    main()
