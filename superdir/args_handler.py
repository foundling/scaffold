import sys
from utils import usage

def get_now():

    import datetime

    dt_now = datetime.datetime.now()
    year, month, day, hour, minute = dt_now.year, dt_now.month, dt_now.day, dt_now.hour, dt_now.minute
    date_label = '{}-{}-{}-{}-{}'.format(year, month, day, hour, minute)

    return date_label

def handle_args(args):
    ''' Args does not include the filename from sys.argv[0] '''

    output_dir, schema = None, None
    date_stamp = 'SUPERDIR_OUTPUT_{}'.format(get_now())

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
