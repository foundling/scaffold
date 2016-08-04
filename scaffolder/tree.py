import utils

def build_tree(schema, indent_size, OUTPUT_DIR):
    ''' Use indentation level of each line relative to the previous indentation level to build a tree structure. '''

    # virtual root provides a way to parse the indentation consistently.  
    virtual_root = utils.new_node(parent=None, name='virtual_root', children=[])
    root = utils.new_node(parent=virtual_root, name=OUTPUT_DIR, children=[])
    virtual_root['children'].append(root)
    parent_node = virtual_root

    indent = -1
    for line in schema:

        new_indent = utils.get_indent(line, indent_size)

        if new_indent > indent:
            parent_node = parent_node['children'][-1]

        elif new_indent < indent:
            depth = indent - new_indent
            parent_node = utils.find_ancestor(parent_node, depth)

        child = utils.new_node(
            parent   = parent_node, 
            name     = utils.get_dirname(line) if utils.is_dir(line) else utils.get_filename(line), 
            children = [] if utils.is_dir(line) else None
        ) 
        parent_node['children'].append(child)

        indent = new_indent

    return virtual_root

def walk_tree(tree, indent, callback):

    for node in tree['children']:
        filename = node['name']
        if node['children'] is not None:
            callback(filename + '/', indent)
            walk_tree(node, indent + 4, callback)
        else:
            callback(filename, indent)


