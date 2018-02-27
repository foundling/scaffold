#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import click

from callbacks import make_config_processor, pprint_node, create_file
from messages import cli_messages as superdir_help 
from tree import Tree
import utils
from validator import Validator

__version_info__ = ('0', '1', '7')
__version__ = '.'.join(__version_info__)

def main(schema=None, output_dir=None, config_path=None):

    """

        Validate the schema file and output directory parameters.
        Build a tree from the schema file.
        Walk the tree, calling the registered callbacks on each node. 

    """

    validator = Validator(schema, output_dir=output_dir)
    validator.validate()

    if not validator.is_valid():
        click.echo(validator.error['msg'])
        sys.exit(1)

    directory_tree = Tree(
        indent_size = validator.indent_size,
        output_dir  = output_dir,
        base_path   = os.path.abspath(os.curdir)
    )
    directory_tree.load_data(schema)
    directory_tree.build_tree()

    callbacks = [ create_file ]

    if config_path:
        process_hooks = make_config_processor(config_path)
        callbacks.append(process_hooks)

    directory_tree.walk(callbacks=callbacks)

def print_version(ctx, param, value):

    if not value or ctx.resilient_parsing:
        return

    click.echo(__version__)
    ctx.exit()

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-v', 
              '--version', 
              is_flag=True, 
              callback=print_version,
              expose_value=False, 
              is_eager=True)

@click.argument('schema_file', 
                type=click.File('r'), 
                required=True, 
                default=sys.stdin)

@click.option('-c', 
              '--config', 
              nargs=1, 
              type=str, 
              help=superdir_help['config'])

@click.option('-o', 
              '--outdir', 
              nargs=1, 
              type=str, 
              help=superdir_help['outdir'])

@click.option('-i', 
              '--indent-string', 
              nargs=1, 
              type=str, 
              help=superdir_help['indent_string'])

def cli(schema_file, config, outdir, indent_string):

    # schema probably coming from a pipe
    if schema_file is None:

        if not sys.stdin.isatty():
            schema = list(sys.stdin) 

    # schema from a file
    else:
        schema = list(schema_file)

    main(schema=schema, output_dir=outdir, config_path=config, indent_string=indent_string)

if __name__ == '__main__':
    cli()
