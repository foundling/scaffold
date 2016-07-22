import pytest
from scaffold import get_indent, validate

f = open('schema.txt')
lines = f.readlines()

def test_get_indent():
    assert get_indent(lines) == 4

def test_validate():
    assert validate(lines, get_indent(lines)) == True

