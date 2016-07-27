import pytest
from scaffolder.scaffolder import get_indent, validate_schema

good_lines = open('good_schema.txt').readlines()
bad_lines = open('bad_schema.txt').readlines()

def test_get_indent():
    assert get_indent(good_lines) == 4

def test_validate_schema():
    assert validate_schema(good_lines, get_indent(good_lines)) == True

