from setuptools import setup

setup(
    name = "scaffolder",
    version = "1.0",
    py_modules = ['scaffolder'],
    install_requires = [
        'scaffolder'
    ],
    entry_points = '''
        [console_scripts]
        scaffolder=scaffolder:main
    '''
)
