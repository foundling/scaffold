![superdir_header](https://github.com/foundling/superdir/blob/master/superdir_logo.png)

`superdir` is a command-line tool for Linux, BSD, and OSX that generates a directory tree from a reasonable, consistently-indented flat file representation.  It is MIT-licensed.

## Installation:

````bash
pip install superdir
````

## Usage:

````bash
$ superdir SCHEMA_FILE [OUTPUT_DIR]
$ cat SCHEMA_FILE | superdir [OUTPUT_DIR]
````

## Contributing

See here for the [contributors guide](https://github.com/foundling/superdir/blob/master/CONTRIBUTING.md). 


## Motivation:

`superdir` is a simple and quick way to generate a directory structure without code.  All you need is a schema file that you can generate yourself or copy from a tutorial you're following along with. Pipe it to `superdir` or pass it as an argument, and off you go.

## Behavior:

- `superdir` will not overwrite any existing files or directories.
- `superdir` creates the directory structure from the schema only if it passes validation.
- By default, lines that end with '`/`' are treated as directories. Everything else is treated as a file. 
- Comments should be prefixed by '`#`'.
- Comments and blank lines are ignored.
- If no `OUTPUT_DIR` argument is given, the schema must contain a single top-level directory.
- If an `OUTPUT_DIR` argument is given, the schema file may contain multiple top-level directories.

## Hooks:

`superdir` will write previously existing template files to the location specified in your schema file if you create a `.superdirrc` file in your home directory that contains the name of the file to look for (the hook) and its location on your system. Here's an example.

````bash
index.html = ~/apps/lib/html/index.html
styles.css = ~/apps/lib/css/styles.css
````

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
