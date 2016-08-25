from setuptools import setup

setup(
    name='Todoapp',
    version='0.1.0',
    py_modules=['todo'],
    install_requires=[
        'Click',
        'colorama',
        'termcolor',
        'pyfiglet',
       
       
    ],
    entry_points='''
        [console_scripts]
        todo=todo:cli
    ''',

)