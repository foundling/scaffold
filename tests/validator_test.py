import os
from StringIO import StringIO

import pytest

from scaffolder.validator import Validator


schema = '''
dir1/
dir2/
'''


def test_val():
    validator = Validator(schema)
    assert validator.schema
