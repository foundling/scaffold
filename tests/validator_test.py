import os
from StringIO import StringIO

import pytest

from superdir.validator import Validator

def test_load_valid_schema():

    schema = '''
    dir1/
    dir2/
        dir3/
            dir4/
    '''.split('\n')

    validator = Validator()
    validator.load_schema(schema)

    assert type(schema) == list
    assert validator.schema is not None
    assert len(validator.schema) > 0
    assert type(validator.schema) == list

def test_passed_validation():

    good_schema = ''' 
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
    '''.split('\n')

    validator = Validator()
    validator.load_schema(good_schema)
    validator.passed_validation()
    indent_size = validator.get_indent_size()

    assert type(good_schema) == list 
    assert indent_size >= 0

def test_failed_validation():

    bad_schema = '''
    dir1/ 
        dir2/
               dir3/
    '''.split('\n')

    validator = Validator()
    validator.load_schema(bad_schema)

    assert type(bad_schema) == list 
    with pytest.raises(SystemExit):
        validator.passed_validation()
