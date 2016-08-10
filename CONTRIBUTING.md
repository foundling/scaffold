# Contributing to Superdir

Superdir is a tiny Python application, but nonetheless, contributions are encouraged, appreciated and welcome! Thanks for even considering the idea!

## Reporting issues

If you find an issue, please ...

- Make sure to search through the [superdir issue tracker](https://github.com/foundling/superdir/issues) first.
- Specify your version of Python and Operating System when reporting an issue.

## Submitting patches

When submitting patches, please ...

- Clearly explain the condition(s) under which Superdir fails and the solution that your patch offers.
- Include tests that clearly show the application 1) failing and 2) the patch resolving this failure.
- Adhere to `PEP8 <http://legacy.python.org/dev/peps/pep-0008/>` where it makes sense.

## Setting up your development environment and running the tests

- You may want to install [virtualenv](https://virtualenv.pypa.io/en/stable/) to host your test environment.
- The only requirement for hacking on Superdir is `py.test`. 

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

