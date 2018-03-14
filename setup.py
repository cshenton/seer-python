#!/usr/bin/env python
from setuptools import setup
import setuptools

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='seer',
    version='0.1',
    description='Python client for cshenton/seer',
    long_description=long_description,
    platforms='MacOS X, Windows, Linux',
    author='Charles Shenton',
    author_email='charlieshenton@me.com',
    url='https://github.com/cshenton/seer-python',
    license='Apache 2.0',
    packages=setuptools.find_packages()
)