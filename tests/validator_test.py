import os
from StringIO import StringIO

import pytest

from superdir.validator import Validator

def test_validate_suceeds():

    good_schema = '''
    dir1/
    dir2/
        dir3/
            dir4/
    '''.split('\n')

    validator = Validator(good_schema)
    assert validator.validate()


def test_validate_fails():

    bad_schema = '''
    dir1/
    dir2/
        dir3/
          dir4/
    '''.split('\n')

    validator = Validator(bad_schema)
    assert not validator.validate()

def test_find_first_indent():

    schema = '''
dir1/
dir2/
    dir3/
        dir4/
    '''.split('\n')

    validator = Validator(schema)
    indent_data = validator._find_first_indent()
    assert indent_data['indent_size'] == 4  
    assert indent_data['index'] == 2
