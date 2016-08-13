#!/usr/bin/env python
# -*- coding: utf-8 -*-



from __future__ import print_function
import datetime
import os
import sys

import click

from tree import Tree
import utils
from validator import Validator
from cli import cli

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

def main(schema=None, output_dir=None, config_path=None):

    BASE_PATH = os.path.abspath(os.curdir)
    indent_size = None

    validator = Validator(output_dir)
    validator.load_schema(schema)
    validator.validate()
    indent_size = validator.get_indent_size()

    directory_tree = Tree(
        indent_size = indent_size,
        output_dir  = output_dir,
        base_path   = BASE_PATH
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
    schema, outfile, config = cli()
    main(schema=schema, output_dir=outfile, config_path=config)
