import sys

import click

@click.command()
@click.option('-o','--outfile', nargs=1, type=str,  help="Filename of the directory to contain your superdir'd files")
@click.option('-c','--config', nargs=1, type=str, help="Config file to read before superdir'ing your schema")
@click.argument('schema_file', type=click.File('r'), required=True, default=sys.stdin)
def handle_args(schema_file, outfile, config):

    schema = None

    if schema_file is None:
        if not sys.stdin.isatty():
            schema = list(sys.stdin) 
    else:
        schema = list(schema_file)

    print 'schema: ', schema
    print 'outfile: ', outfile
    print 'config: ', config

if __name__ == '__main__':
    handle_args()


'''

interface:

standard
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
