import os
from StringIO import StringIO

import pytest

from scaffolder.validator import Validator


def test_load_schema():

    assert Validator(good_schema).schema

def test_validate():

    assert Validator(good_schema).validate()

    with pytest.raises(ValueError):
        assert Validator(bad_schema).validate()
