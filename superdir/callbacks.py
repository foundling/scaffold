# -*- coding: utf-8 -*-

import os
import sys

import pprint
import utils

pp = pprint.PrettyPrinter(indent=1)

def pprint_node(node):
    pp.pprint(node)

def create_file(node):
    """ 

    Create a regular file if node has NoneType for children,  
    otherwise, creates a directory. 

    


    """

    if node['data']['filename'] == os.path.abspath(os.curdir):

        print('Error: you have specified the current directory as your' 
               'output directory. Create a new directory. See superdir --help'
               'for usage');

        sys.exit(1) 

    if os.path.exists(node['data']['basedir']):

        print('Error, the directory {} already exists'.format(node['data']['basedir']))
        sys.exit(1) 

    if node['children'] is None:

        try:
            open(node['data']['basedir'], 'w').close()

        except IOError as E:
            print('Error: could not create regular file: {}.'.format(node['data']['basedir']))
            print(E)
    else:

        try:
            os.mkdir(node['data']['basedir'])

        except IOError as E:
            print('Error: could not create directory: {}.'.format(node['data']['basedir']))
            print(E)

def make_config_processor(config_path=None):
    ''' Takes relative name of config file in ~/home directory ''' 

    full_path = os.path.abspath( os.path.join(os.path.expanduser('~'), config_path) )

    try:
        with open(full_path) as config_file:
            hooks = dict([  
                            map(str.strip, line.split('=')) 
                            for line in config_file  
                            if line.strip() 
            ])

    except IOError as E:
        print('Could not open config file.')
        print(E)
        sys.exit(1)

    def process_config_hooks(node):
        ''' on each node, if there's a match in the config settings, that file is created. '''

        filename = node['data']['filename']
        if filename in hooks:

            try:
                with open( hooks[filename], 'r' ) as src_file, open( node['data']['basedir'], 'w' ) as dst_file:
                    dst_file.write( src_file.read() ) 

            except IOError as E:
                print('Could not write config hook to new file.')
                print(E)
                sys.exit(1)

    return process_config_hooks
