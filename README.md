![superdir_header](https://github.com/foundling/superdir/blob/master/superdir_logo.png)
`superdir` is a command-line tool for Linux, BSD, and OSX that generates a directory tree from a reasonable, consistently-indented flat file representation.  It is MIT-licensed.

## Installation:

````bash
pip install Superdir
````

## Usage:

````bash
superdir SCHEMA_FILE [OUTPUT_DIR]
````

## Rules:

- `superdir` creates the directory structure from the schema only if it passes validation.
- By default, lines that end with '`/`' are treated as directories. Everything else is treated as a file. 
- Comments are prefixed with a '`#`'.
- Comments and blank lines are ignored.
- If an `OUTPUT_DIR` argument is **not** given, the schema must contain a single top-level directory.
- If an `OUTPUT_DIR` argument is given, the schema file may contain multiple top-level directories.
- If the `OUTPUT_DIR` already exists, it won't be overwritten. 

## An example:

````bash
$ cat schema.txt

# Flat-file example of a directory structure
superdir/
    docs/
    superdir/
        superdir.py
        validator.py
        tree.py
    test/
        superdir_test.py
        validator_test.py
        tree_test.py
    README.md
    LICENSE.md
    test/

$ superdir schema.txt new_project 
````
This gets turned into a directory tree rooted at `new_project` within your current directory. 

````
$ tree
new_project
└── superdir/
    └── docs/
    └── superdir/
        └── superdir.py
        └── validator.py
        └── tree.py
    └── test/
        └── superdir_test.py
        └── validator_test.py
        └── tree_test.py
    └── README.md
    └── LICENSE.md
````

