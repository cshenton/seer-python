#!/usr/bin/env python
from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='seer',
    version='0.1.1',
    description='Python client for cshenton/seer',
    long_description=long_description,
    platforms='MacOS X, Windows, Linux',
    author='Charles Shenton',
    author_email='charlieshenton@me.com',
    url='https://github.com/cshenton/seer-python',
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*",
    install_requires=[
        'grpcio',
        'grpcio-tools',
        'protobuf',
        'six',
    ],
    license='Apache 2.0',
    packages=['seer'],
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)