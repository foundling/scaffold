![superdir_header](https://github.com/foundling/superdir/blob/master/superdir_logo.png)

`superdir` is a command-line tool for Linux, BSD, and OSX that generates a directory tree from a reasonable, consistently-indented flat file representation.  It is MIT-licensed.

## Installation:

````bash
pip install superdir
````

## Usage:

````bash

$ superdir schema.txt 

$ superdir schema.txt -o new_app 

# read from stdin
$ superdir schema.txt -- 

# pipe data in
$ cat schema.txt | superdir -o new_app

````

## Contributing

See here for the [contributors guide](https://github.com/foundling/superdir/blob/master/CONTRIBUTING.md). 


## Motivation:

`superdir` is a simple and quick way to generate a directory structure without code.  All you need is a schema file that you can generate yourself or copy from a tutorial you're following along with. Pipe it to `superdir` or pass it as an argument, and off you go.

## Behavior:

- `superdir` will not overwrite any existing files or directories and creates the directory structure from your schema only if it passes validation.
- By default, lines that end with '`/`' are treated as directories. Everything else is treated as a file. 
- Comments should be prefixed by '`#`'.
- Comments and blank lines are ignored.
- If no `OUTPUT_DIR` option is given, the schema must contain exactly one top-level directory.
- If an `OUTPUT_DIR` option is given, the schema file may contain one or more top-level directories and or files.

## Hooks:

Hooks will let you write the content of a template file to all matching filenames in your schema file. To take advantage of hooks, create a `.superdirrc` file in your home directory. Add an equals-separated key-value pair for each template file you want, where the key is the filename and the value is the template file's location on your system. Here's an example:

````bash
# config file in $HOME/.superdirrc 

# pattern to match from schema -> template location 
index.html = ~/apps/lib/html/index.html
styles.css = ~/apps/lib/css/styles.css

````

In the process of building the tree, if `superdir` comes across a matching file key, it will write the corresponding content from the file into the file tree's resulting file.

## superdir in action!

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
$ cat schema.txt | superdir another_new_project
$ tree another_new_project
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
