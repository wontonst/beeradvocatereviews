"""
Setup beeradcovatereviews module.
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='beeradvocatereviews',
    version='1.0.4',

    description='Module to export user reviews',
    long_description=long_description,
    url='https://github.com/wontonst/beeradvocatereviews',
    author='Roy Zheng',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ],
    keywords='beeradvocate beer api',
    install_requires=['pyquery', 'requests'],
    packages=['beeradvocatereviews'],
    entry_points={
        'console_scripts': [
            'beeradvocatereviews=beeradvocatereviews.__main__:main',
        ],
    },
)
