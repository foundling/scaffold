# -*- coding: utf-8 -*-

import os

import utils

def create_file(node):
    ''' Create a regular file if node has NoneType for children.  Otherwise, creates a directory. '''

    if node['children'] is None:
        open(node['path'], 'w').close()
    else:
        os.mkdir(node['path'])

def make_config_processor(config_path=None):
    ''' Takes relative name of config file in ~/home directory ''' 

    if config_path is None:
        return


    # TODO
    # split config file on '=' and clean results
    # make a map of filename to file path
    full_path = os.path.abspath( os.path.join(os.path.expanduser('~'), config_path) )
    with list(open(full_path)) as config:
        pass

    def process_config_hooks(node):
        ''' on each node, if there's a match in the config settings, that file is created. '''

        # TODO
        # if node['value'] matches filename, write filepath to node['path']


    return process_config_hooks



