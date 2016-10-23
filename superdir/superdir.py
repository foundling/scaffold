#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys

import click

from tree import Tree
from validator import Validator
from callbacks import make_config_processor, create_file
import utils
from messages import cli_messages as superdir_help 

__version_info__ = ('0', '1', '7')
__version__ = '.'.join(__version_info__)

def main(schema=None, OUTPUT_DIR=None, CONFIG_PATH=None):
    """

    - Validate the schema file and output directory parameters
    - Build a tree from the schema file
    - Walk the tree, calling the registered callbacks on each node. 

    """

    validator = Validator(schema, OUTPUT_DIR=OUTPUT_DIR)
    if not validator.validate():
        click.echo(validator.error['msg'])
        sys.exit(1)

    directory_tree = Tree(
        INDENT_SIZE = validator.INDENT_SIZE,
        OUTPUT_DIR  = OUTPUT_DIR,
        base_path   = os.path.abspath(os.curdir)
    )
    directory_tree.load_data(schema)
    directory_tree.build_tree()

    callbacks = [ create_file ]

    if CONFIG_PATH:
        process_hooks = make_config_processor(CONFIG_PATH)
        callbacks.append(process_hooks)

    directory_tree.walk(callbacks=callbacks)

def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(__version__)
    ctx.exit()

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-v', '--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
@click.argument('schema_file', type=click.File('r'), required=True, default=sys.stdin)
@click.option('-c', '--config', nargs=1, type=str, help=superdir_help['config'])
@click.option('-o', '--outdir', nargs=1, type=str, help=superdir_help['outdir'])
def cli(schema_file, outdir, config):

    schema = None

    if schema_file is None:

        # schema probably coming from a pipe
        if not sys.stdin.isatty():
            schema = list(sys.stdin) 

    else:

        # schema from a file
        schema = list(schema_file)


    main(schema=schema, OUTPUT_DIR=outdir, CONFIG_PATH=config)

if __name__ == '__main__':

    cli()
