#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

CLI interface:

[ standard ]
    superdir schema.txt [ -o my_app ]

standard, uses schema's top-level dir (throws if there's more than one top level anything) 
    superdir schema.txt 

pipe
    cat schema.txt | superdir [ -o my_app ]

help
    superdir -h, --help

specify a config
    superdir -c config

'''

from __future__ import print_function
import datetime
import os
import sys

import click

from tree import Tree
import utils
from validator import Validator

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

def superdir(schema=None, output_dir=None, config_path=None):

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

@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('-o','--outfile', nargs=1, type=str,  help="Directory name to contain your superdir'd files."
                                                         "If none is suppied, your schema file must have exactly"
                                                         "one top-level directory and no sibling regular files."
                                                         "That top-level directory will be the parent of your new"
                                                         "file tree.")
@click.option('-c','--config', nargs=1, type=str, help="Config file to read before superdir'ing your schema.")
@click.argument('schema_file', type=click.File('r'), required=True, default=sys.stdin)
def main(schema_file, outfile, config):

    schema = None

    if schema_file is None:
        if not sys.stdin.isatty():
            schema = list(sys.stdin) 
    else:
        schema = list(schema_file)

    superdir(schema=schema, output_dir=outfile, config_path=config)


if __name__ == '__main__':
    main()
