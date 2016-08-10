from setuptools import setup

setup(
    name = "superdir",
    version = "0.1.0",
    py_modules = ['superdir'],
    install_requires = [
        'superdir'
    ],
    entry_points = '''
        [console_scripts]
        superdir=superdir:main
    '''
)
