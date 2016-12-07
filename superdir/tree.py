# -*- coding: utf-8 -*-

import os
import utils

class Tree:

    def __init__(self, output_dir=None, base_path=None, indent_size=None):

        self.output_dir = output_dir
        self.base_path = base_path
        self.indent_size = indent_size
        self.input = None
        self.virtual_root = dict(
            parent = None,
            children = [],
            data = { 
                'filename': None, 
                'basedir': self.base_path 
            },
        )
        self.root = dict(
            parent = self.virtual_root,
            children = [],
            data = { 
                'filename': self.output_dir, 
                'basedir': ( 
                    os.path.join(self.base_path, self.output_dir) 
                    if self.output_dir 
                    else self.base_path 
                )
            },
        )
        self.virtual_root.append(self.root);

    def build_tree(self):

        """

        Build tree using indentation level.

        Indentation indicates a change in hierarchy level.
        current line ending in '/' or not indicates regular file or not.

        The question in this loop: where to put this new line?, 
        which is asking "who is the parent of new line?"

        """ 

        parent_node = self.virtual_root
        prev_indent = -1

        for line in self.input:

            cur_indent = utils.get_indent_count(line, self.indent_size)
            distance = cur_indent - prev_indent
            # who is the parent?
            parent_node = self._find_new_parent(parent_node, distance)
            filename = (utils.get_dirname(line)
                        if utils.is_dir(line)
                        else utils.get_filename(line))

            child = dict(
                parent = parent_node, 
                children = [] if utils.is_dir(line) else None,
                data = { 
                    'filename': filename, 
                    'basedir': os.path.join(parent_node['data']['basedir'], filename) 
                },  
            ) 

            parent_node['children'].append(child)
            prev_indent = cur_indent

    def _find_new_parent(self, parent_node, distance):

        new_parent = parent_node

        if distance > 0:
            new_parent = parent_node['children'][-1]

        elif distance < 0:
            new_parent = self._find_ancestor(parent_node, abs(distance))

        return new_parent

    def walk(self, callbacks):
        ''' Walk tree and call callback on each node. '''

        def _walk(tree):

            children = tree['children']

            for child in children:

                if callbacks:
                    for cb in callbacks:
                        cb(child)

                if child['children'] is not None:
                    _walk(child)

        tree = self.virtual_root
        _walk(tree)

    def load_data(self, data):

        ''' Load and clean up input data '''

        self.input = utils.clean(data)

    def _find_ancestor(self, start_node, parents_to_visit):

        ''' Return parent directory corresponding to node parsed from current line. '''

        current_node = start_node

        while (parents_to_visit > 0):
            current_node = current_node['parent']
            parents_to_visit -= 1

        return current_node
