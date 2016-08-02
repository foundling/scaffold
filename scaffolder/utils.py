def chomp(line): 
    return line[:-1]

def is_empty(line):
    return line.strip()

def is_comment(line):
    return line.lstrip().startswith('#')

def is_dir(line):
    return line.rstrip().endswith('/')

def get_indent(line):
    return len(line) - len(line.lstrip())

def get_filename(line):
    return line.strip()

def get_dirname(line):
    return line.strip().rstrip('/')

def new_node(parent, dirname):
    return  dict(parent=parent, dirname=dirname, children=[])

def new_leaf(parent, filename):
    return dict(parent=parent, filename=filename)

def find_ancestor(start_node, parents_to_visit):
    ''' Use relative dedent level to determine parent.
        1 dedent -> append new node to parent's parent's child node  
        N is a unit of dedent, then we travel up N + 1 parents and append a new node to its children
    '''
    current_node = start_node

    while (parents_to_visit > 0):
        current_node = current_node['parent']
        parents_to_visit -= 1

    return current_node

def validate_schema(schema):
    ''' Takes in a list of lines and returns indentation size if valid, throws if invalid. '''

    indent_size = 4

    return indent_size

def walk_tree(root, indent):
    for child in root['children']:
        if type(child) == dict:
            print ''.join([ child['dirname'], '/' ]) 
            walk_tree(child, indent + 4)
        else:
            print indent * ' ' + child

def build_tree(schema, indent_size):

    root = new_node(None, 'root')
    current_node = root
    last_indent = 0

    #pdb.set_trace()
    for line in schema:
        indent = get_indent(line)
        filename = get_filename(line) 

        if indent > last_indent:
            ''' We are creating a directory, which means a new child node of the most recent directory. '''

            # get last node created in current node's children, becomes parent of new dir node  
            parent = current_node['children'][-1]

            # if this line represents a directory, create a new node, append to parent's children
            # and set current node that node
            if is_dir(line):
                dirname = get_dirname(line)
                new_dir_node = new_node(parent, dirname)
                parent['children'].append(new_dir_node)
                current_node = new_dir_node

                # update last_indent because we've entered a new indentation level 
                last_indent = indent

            else:
                # otherwise, append its filename to parent's children
                file_name = get_filename(line)
                parent['children'].append(file_name)


        elif indent < last_indent:
            ''' We are creating a new node at the level of the parent or higher in the tree '''

            # how many 'units' of indent is it less than current? call that n
            # traverse N + 1 parents 

            n = (last_indent - indent) / indent_size
            parents_to_visit = n + 1
            target_parent = find_ancestor(current_node, parents_to_visit)

            if is_dir(line):
                parent = target_parent
                dirname = get_dirname(line)
                target_parent['children'].append(parent, dirname)
            else:
                filename = get_filename(line)
                target_parent['children'].append(filename)

            # now set the current node to be target parent
            current_node = target_parent


        else:
            ''' Just adding more dirs or files to the current node's children '''

            #print ''' adding children to current node '''
            if is_dir(line):
                parent = current_node['parent']
                dirname = get_dirname(line)
                new_dir_node = new_node(parent, dirname)
                current_node['children'].append(new_dir_node)
            else:
                filename = get_filename(line)
                current_node['children'].append(filename) 


    return root

def main():

    schema_file = '2test.txt'
    # remove newlines and filter out empty lines
    schema = [  chomp(line) 
                for line in open(schema_file).readlines() 
                if not is_empty(line) or not is_comment(line) ]

    indent_size = validate_schema(schema)
    tree = build_tree(schema, indent_size)
    #walk_tree(tree, 0)

if __name__ == '__main__':
    main()
