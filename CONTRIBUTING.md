# Contributing to Superdir

## Reporting issues

- Please make sure to specify your version of Python and the OS when reporting an issue.
- Please make sure to read through the GitHub issues for `superdir` before you post an issue.

## Submitting patches

- Explain the solution your patch offers.
- Include tests that clearly demonstrate application 1) failing and 2) the patch resolving this failure.
- Code style and clarity is paramount. Please adhere to `PEP8 <http://legacy.python.org/dev/peps/pep-0008/>` where it makes sense when submitting a patch.

# Running Tests

- You probably want to install `virtualenv` for your test environment.
- The only requirement for developing Superdir is `py.test`. 

Install Superdir as an editable package using the current source::

````bash
    # clone the superdir repo
    git clone https://github.com/foundling/superdir.git

    # cd into the top-level directory 
    cd superdir

    # pip install it as an editable package
    pip install --editable .

    # run py.tests
    py.test
````

Running test coverage
---------------------
Generating a report of lines that do not have unit test coverage can indicate where
to start contributing.  ``pytest`` integrates with ``coverage.py``, using the ``pytest-cov``
plugin.  This assumes you have already run the testsuite (see previous section)::

    pip install pytest-cov

After this has been installed, you can output a report to the command line using this command::

    py.test --cov=flask tests/

Generate a HTML report can be done using this command::

    py.test --cov-report html --cov=flask tests/

Full docs on ``coverage.py`` are here: https://coverage.readthedocs.io
