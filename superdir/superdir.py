#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys

import click

from tree import Tree
from validator import Validator
from cli import cli
import utils


def create_file(node):
    ''' File creation callback to run on each tree node. '''

    file_to_create = node['path']
    if node['children'] is None:
        open(file_to_create,'w').close()
    else:
        os.mkdir(file_to_create)

def main(schema=None, output_dir=None, config_path=None):
    ''' '''

    BASE_PATH = os.path.abspath(os.curdir)

    indent_size = None
    validator = Validator(output_dir)
    validator.load_schema(schema)
    validator.validate_indent()
    indent_size = validator.get_indent_size()

    directory_tree = Tree(
        indent_size = indent_size,
        output_dir  = output_dir,
        base_path   = BASE_PATH
    )
    directory_tree.load_data(schema)
    directory_tree.build_tree()


    directory_tree.walk(callback=create_file)


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.argument('schema_file', type=click.File('r'), required=True, default=sys.stdin)
@click.option('-c', '--config', nargs=1, type=str, help="Config file to read before superdir'ing your schema.")
@click.option('-o', '--outfile', nargs=1, type=str, help=("Directory name to contain your superdir'd files. If none is" 
                                                          "supplied, your schema file must have exactly one top-level directory"         
                                                          "and no sibling regular files. That top-level directory will be the"
                                                          "parent of your new file tree."))
def cli(schema_file, outfile, config):

    schema = None

    if schema_file is None:
        # schema probably coming from a pipe
        if not sys.stdin.isatty():
            schema = list(sys.stdin) 

    else:
        # schema from a file
        schema = list(schema_file)

    main(schema=schema, output_dir=outfile, config_path=config)

if __name__ == '__main__':

    cli()

