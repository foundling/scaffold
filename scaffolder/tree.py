import utils
import pdb

class Tree:

    def __init__(self, indent_size, output_dir):

        self.indent_size = indent_size
        self.output_dir = output_dir
        self.data = None
        self.root = None

    def build_tree(self):
        ''' Derive parent/child hierarchy from relationship in indentation between current and previous line.  '''

        virtual_root = self._make_new_node(
            parent=None,
            value='virtual_root',
            children=[]
        )

        root = self._make_new_node(
            parent=virtual_root,
            value=self.output_dir, 
            children=[]
        )

        virtual_root['children'].append(root)

        parent_node = virtual_root
        indent = -1

        for line in self.data:

            new_indent = utils.get_indent(line, self.indent_size)

            if new_indent > indent:
                parent_node = parent_node['children'][-1]

            elif new_indent < indent:
                distance = indent - new_indent
                parent_node = self._find_ancestor(parent_node, distance)

            child = self._make_new_node(
                parent   = parent_node, 
                value    = utils.get_dirname(line) if utils.is_dir(line) else utils.get_filename(line), 
                children = [] if utils.is_dir(line) else None
            ) 

            parent_node['children'].append(child)
            indent = new_indent

        self.root = virtual_root

    def walk(self, callback):
        ''' The contract with Tree: args are a dict with parent, children and value properties. '''

        tree = self.root
        
        def _walk(tree):

            for node in tree['children']:

                callback(node)
                if node['children'] is not None:
                    _walk(node)

        _walk()

    def _load_data(self, data):
        ''' loads the input data, cleans it '''
        this.data = utils.clean(data)

    def _make_new_node(self, parent=None, value=None, children=None):
        ''' create a new node. if children is Nonetype, node is treated as a leaf. '''
        return  dict(parent=parent, value=value, children=children)

    def _find_ancestor(self, start_node, parents_to_visit):
        ''' use indentation level relative to previous line to find ancestor.'''
        current_node = start_node

        while (parents_to_visit > 0):
            current_node = current_node['parent']
            parents_to_visit -= 1

        return current_node
