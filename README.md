[![Build Status](https://travis-ci.org/foundling/superdir.svg?branch=master)](https://travis-ci.org/foundling/superdir)

[![PyPI version](https://badge.fury.io/py/superdir.svg)](https://badge.fury.io/py/superdir)

![superdir_header](https://github.com/foundling/superdir/blob/master/media/superdir_logo.png)

`superdir` is a command-line tool for Linux, BSD, and OSX that generates a directory tree from a reasonable, consistently-indented flat file representation.  It is MIT-licensed.

## Installation:

````bash
pip install superdir
````

## Dependencies

````bash
click
````

## Usage:

````bash

Usage: superdir [OPTIONS] SCHEMA_FILE

Options:
  -o, --outfile TEXT  Filename of the directory to contain your superdir'd
                      files
  -c, --config TEXT   Config file to read before superdir'ing your schema
  -h, --help          Show this message and exit.

````

## Contributing

See here for the [contributors guide](https://github.com/foundling/superdir/blob/master/CONTRIBUTING.md). 


## Motivation:

`superdir` is a simple and quick way to generate a directory structure without code.  All you need is a schema file that you can generate yourself or copy from a tutorial you're following along with. Pipe it to `superdir` or pass it as a filename argument, and off you go.

## Behavior:

- `superdir` will not overwrite any existing files or directories and creates the directory structure from your schema only if it passes validation.
- By default, lines that end with '`/`' are treated as directories. Everything else is treated as a file. 
- Comments should be prefixed by '`#`'.
- Comments and blank lines are ignored.
- If no `OUTPUT_DIR` option is given, the schema must contain exactly one top-level directory with no sibling files.
- If an `OUTPUT_DIR` option is given, the schema file may contain one or more top-level directories and or files.

## Hooks:

Hooks will let you copy a pre-existing file's content into a file created from your schema. To take advantage of hooks, pass the `-c` or `--config` flag with a filepath relative to your $HOME directory. In the config file, add an equal-delimited list of key-value pairs, where the key is the filename and the value is the filepath for the file you want to copy. Here's an example:

````bash
# config file in $HOME/.superdir_hooks 

# pattern to match from schema -> template location 
index.html = ~/apps/lib/html/index.html
styles.css = ~/apps/lib/css/styles.css

````

In the process of building the tree, if `superdir` comes across a matching file key, it will write the corresponding content from the file into the file tree's resulting file.

## superdir in action!

````bash

# this a valid schema file
$ cat schema.txt
superdir/
    docs/
    # comments and blank lines are ignored
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

# creating a directory tree from the schema file
$ superdir schema.txt -o new_project && tree new_project 
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

# Piping schema.txt into superdir 
$ cat schema.txt | superdir -o another_new_project && tree another_new_project
another_new_project
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
