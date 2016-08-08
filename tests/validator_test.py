import os
from StringIO import StringIO

from scaffolder import validator

@pytest.yield_fixture(autouse_True)
def make_validator():
    Validator = validator
    pass
