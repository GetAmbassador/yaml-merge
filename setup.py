from distutils.core import setup

setup(
    name='yaml-merge',
    version='0.1',
    packages=['.',],
    license='The MIT License',
    author="The engineering Diplomats at Ambassador",
    entry_points = {
        'console_scripts': ['yaml-merge=main:main'],
    }
)
