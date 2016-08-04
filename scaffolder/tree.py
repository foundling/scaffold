import utils
import pdb

class Tree:

    def __init__(self, schema, indent_size, OUTPUT_DIR):
        self.schema = schema
        self.indent_size = indent_size
        self.OUTPUT_DIR = OUTPUT_DIR
        self.tree = None

    def build_tree(self):
        ''' Use indentation level of each line relative to the previous indentation level to build a tree structure. '''

        # virtual root provides a way to parse the indentation consistently.  
        virtual_root = self.make_new_node(parent=None, name='virtual_root', children=[])
        root = self.make_new_node(parent=virtual_root, name=self.OUTPUT_DIR, children=[])
        virtual_root['children'].append(root)
        parent_node = virtual_root

        indent = -1
        for line in self.schema:

            new_indent = utils.get_indent(line, self.indent_size)

            if new_indent > indent:
                parent_node = parent_node['children'][-1]

            elif new_indent < indent:
                depth = indent - new_indent
                parent_node = self.find_ancestor(parent_node, depth)

            child = self.make_new_node(
                parent   = parent_node, 
                name     = utils.get_dirname(line) if utils.is_dir(line) else utils.get_filename(line), 
                children = [] if utils.is_dir(line) else None
            ) 
            parent_node['children'].append(child)
            indent = new_indent

        self.tree = virtual_root

    def make_new_node(self, parent=None, name=None, children=None):
        ''' Create a new node. If children is NoneType, node is treated as a leaf. '''
        return  dict(parent=parent, name=name, children=children)

    def find_ancestor(self, start_node, parents_to_visit):
        ''' Use indentation level relative to previous line to find ancestor.'''
        current_node = start_node

        while (parents_to_visit > 0):
            current_node = current_node['parent']
            parents_to_visit -= 1

        return current_node

    def walk_tree(self, tree, indent, callback):

        for node in tree['children']:
            filename = node['name']
            if node['children'] is not None:
                callback(filename + '/', indent)
                self.walk_tree(node, indent + self.indent_size, callback)
            else:
                callback(filename, indent)
