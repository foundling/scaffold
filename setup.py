from setuptools import setup

setup(
    name = "scaffold",
    version = "1.0",
    py_modules = ['scaffold'],
    install_requires = [
        'scaffold'
    ],
    entry_points = '''
        [console_scripts]
        scaffold=scaffold:main
    '''
)
