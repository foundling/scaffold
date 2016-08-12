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
    '''

    validator = Validator()
    validator.load_schema(schema)

    assert validator.schema is not None
    assert len(validator.schema) > 0
    assert type(validator.schema) == list

def test_validate_success():

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
    '''

    validator = Validator()
    validator.load_schema(good_schema)
    validator.validate()
    indent_size = validator.get_indent_size()

    assert indent_size >= 0

def test_validate_failure():

    bad_schema = '''
    dir1/ 
        dir2/
               dir3/
    '''.split('\n')

    validator = Validator()
    validator.load_schema(bad_schema)
    with pytest.raises(SystemExit):
        validator.validate()


