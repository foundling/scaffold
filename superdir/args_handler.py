# -*- coding: utf-8 -*-

import sys

import click

from utils import usage


def output_dir_name(dir_suffix = 'SUPERDIR_OUTPUT', datestring=None):
    ''' Appends a current date in YYYY-MM-DD-HH-MM format to a directory suffix. '''

    if datestring is None:
        import datetime

        dt_now = datetime.datetime.now()
        year, month, day, hour, minute = dt_now.year, dt_now.month, dt_now.day, dt_now.hour, dt_now.minute
        datestring = '{}-{}-{}-{}-{}'.format(year, month, day, hour, minute)

    output_dir_name = '{}-{}'.format(dir_suffix, datestring)

    return output_dir_name

def handle_args_old(args):
    ''' Args does not include the filename from sys.argv[0] '''

    output_dir, schema = None, None
    date_stamp = 'SUPERDIR_OUTPUT_{}'.format(current_datestamp())

    if sys.stdin.isatty():

        # superdir schema.txt [ new_app ]

        if len(args) == 1:
            output_dir = date_stamp 

        if len(args) == 2:
            output_dir = args[-1]

        else:
            usage()
            exit(1)

        with open(args[0]) as fh:
            schema = [ line for line in fh ]


    else:

        # cat schema.txt | superdir [ new_app ]

        if len(args) == 0:
            output_dir = date_stamp 

        elif len(args) == 1:
            output_dir = args[-1]

        else: 
            usage()
            exit(1)

        schema = list(sys.stdin)

    return schema, output_dir
