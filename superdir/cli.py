#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''CLI interface:

superdir schema.txt [ -o my_app ]
superdir schema.txt 
cat schema.txt | superdir [ -o my_app ]
superdir -h, --help
superdir -c config

'''

import sys

import click

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.argument(
    'schema_file',\
    type=click.File('r'),\
    required=True,\
    default=sys.stdin)
@click.option(
    '-c',\
    '--config',\
    nargs=1,\
    type=str,\
    help="Config file to read before superdir'ing your schema.")
@click.option(
    '-o',
    '--outfile', 
    nargs=1,
    type=str,
    help='''Directory name to contain your superdir'd files. If none is 
         supplied, your schema file must have exactly one top-level directory 
         and no sibling regular files. That top-level directory will be the 
         parent of your new file tree.''')
def cli(schema_file, outfile, config):

    schema = None

    if schema_file is None:
        # pipe
        if not sys.stdin.isatty():
            schema = list(sys.stdin) 

    else:
        # file
        schema = list(schema_file)

    return schema, outfile, config
