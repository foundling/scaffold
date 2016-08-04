# Scaffolder

Scaffolder generates a directory tree from a reasonable, consistently-indented flat file representation of a directory structure. 

here's an example:

````bash
$ cat schema.txt

scaffolder/
    docs/
    license.md
    scaffolder/
        scaffolder.py
        validator.py
        tree.py
        test/
            scaffolder_test.py
            validator_test.py
            tree_test.py
        readme.md
        license.md
    readme.md
    test/

$ scaffolder schema.txt new_project 
````
This gets turned into a directory tree in your current directory. 

````
$ tree
.
└── scaffolder/
    └── docs/
    └── license.md
    └── scaffolder/
        └── scaffolder.py
        └── validator.py
        └── tree.py
    └── test/
        └── scaffolder_test.py
        └── validator_test.py
        └── tree_test.py
    └── readme.md
    └── license.md

````

# Rules:
    - the indentation level must be consistent throughout the schema file. 
    - lines that end with a '/' are directories. everything else is a file. 
    - if a command-line argument for the root directory is not given, the schema must contain a 
    single top-level directory.
    - if a command-line argument for the root directory is given, multiple top-level directories 
    are allowed.
    - blank lines (lines of length 0 after being stripped of whitespace) and comments (lines starting with 
    '#' after
    being stripped of whitespace) are ignored.
    - indentation must be preceded by a directory.
