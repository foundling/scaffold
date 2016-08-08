# Scaffolder

Scaffolder generates a directory tree from a reasonable, consistently-indented flat file representation of a directory structure. 

Here's an example:

````bash
$ cat schema.txt

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
This gets turned into a directory tree in your current directory. 

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

# Rules:
- The indentation level must be consistent throughout the schema file. 
- Lines that end with a '/' are directories. everything else is a file. 
- If a command-line argument for the root directory is not given, the schema must contain a 
single top-level directory.
- If a command-line argument for the root directory is given, multiple top-level directories 
are allowed.
- Blank lines (lines of length 0 after being stripped of whitespace) and comments (lines starting with 
'#' after
being stripped of whitespace) are ignored.
- Indentation must be preceded by a directory.
