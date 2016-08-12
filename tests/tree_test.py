import os
from StringIO import StringIO

from superdir.tree import Tree
from superdir.utils import clean

def test_tree_obj():

    schema = ''' 
    app/
        app/

            app.py
            lib.py
    # Comment

        docs/
        tests/
            app_test.py
            lib_test.py
    etc/
    '''

    new_tree = Tree(
        indent_size = 4,
        output_dir = 'new_app',
    )

    new_tree.load_data(schema)

    assert new_tree.data is not None
    assert new_tree.indent_size == 4 
    assert new_tree.output_dir == 'new_app'

def test_build_tree():

    schema = ''' 
    app/
        app/

            app.py
            lib.py
    # Comment

        docs/
        tests/
            app_test.py
            lib_test.py
    etc/
    '''


    tree = Tree(
        indent_size = 4,
        output_dir = 'new_app',
        base_path = os.path.abspath(os.curdir)
    )
    tree.load_data(schema)
    tree.build_tree()

    assert tree.root is not None
    assert os.path.join(os.path.abspath(os.curdir), 'new_app') == os.path.join(tree.base_path, tree.output_dir)  


def test_walk():
    pass

def test_load_data():
    pass

def test_make_new_node():
    pass

def test_find_ancestor():
    pass

