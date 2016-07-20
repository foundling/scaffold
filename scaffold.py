import sys
import os

scaffold_file, output_path = sys.argv[1:3]

def err(msg):
    print msg
    sys.exit(1)

def determine_indendation():
    pass

def validate(text):
    ''' 
        Go through each line and get leading spaces count. If at any point
        the present indentation does not match the previous ones, Raise Exception.
    '''

    return text


def parse():
    pass


def main():

    try:
        f = open(scaffold_file)
        text = f.read()

    except IOError:
        msg = 'Error: Cannot open file {}.'.format(scaffold_file)
        if not os.path.exists(scaffold_file):
            msg += ' The file doesn\'t exist.'
            
        err(msg)

    try:
        # use os.path correctly to get the full path
        output_dir = os.mkdir(output_path)

    except OSError:
        msg = 'The directory exists. I wont overwrite it.' 


    validate(text)

if __name__ == '__main__':
    main()
