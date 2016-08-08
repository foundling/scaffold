# Scaffolder

Scaffolder is a command-line tool for Linux, OSX and WIndows that generates a directory tree from a reasonable, consistently-indented flat file representation.

## Installation:

````bash
pip install Scaffolder
````

## Usage:

````bash
scaffolder SCHEMA_FILE [OUTPUT_DIR]
````

## Rules:

- Scaffolder will only create a directory structure if the schema file passes validation for consistent indentation.
- By default, lines that end with '`/`' are treated as directories. Everything else is treated as a file. 
- Indentation must be preceded by a directory.
- Comments are prefixed with a '`#`'.
- Comments and blank lines are ignored.
- If an `OUTPUT_DIR` argument is **not** given, the schema must contain a single top-level directory.
- If an `OUTPUT_DIR` argument is given, multiple top-level directories are allowed in the schema file.
- If the `OUTPUT_DIR` already exists, it won't be overwritten. 
- Blank lines (lines of length 0 after being stripped of whitespace) and comments (lines starting with '#' after being stripped of whitespace) are ignored.

## An Example:

````bash
$ cat schema.txt

# Flat-file example of a directory structure
scaffolder/
    docs/
    scaffolder/
        scaffolder.py
        validator.py
        tree.py
    test/
        scaffolder_test.py
        validator_test.py
        tree_test.py
    README.md
    LICENSE.md
    test/

$ scaffolder schema.txt new_project 
````
This gets turned into a directory tree rooted at `new_project` within your current directory. 

````
$ tree
new_project
└── scaffolder/
    └── docs/
    └── scaffolder/
        └── scaffolder.py
        └── validator.py
        └── tree.py
    └── test/
        └── scaffolder_test.py
        └── validator_test.py
        └── tree_test.py
    └── README.md
    └── LICENSE.md
````

