#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

python_requirements = '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*'
requirements = ['configparser',
                'packaging~=18.0',
                'paramiko',
                'pytest~=3.6',
                'setuptools',
                'sh',
                'shade']
packages = ['pytest_rpc']
entry_points = {
    'pytest11': [
        'rpc=pytest_rpc',
    ],
}

setup(
    name='pytest-rpc',
    version='1.1.1-dev0',
    author='rpc-automation',
    author_email='rpc-automation@rackspace.com',
    license='Apache Software License 2.0',
    url='https://github.com/rcbops/pytest-rpc',
    keywords='py.test pytest pytest-rpc',
    description='Extend py.test for RPC OpenStack testing.',
    long_description=readme + '\n\n' + history,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    include_package_data=True,
    python_requires=python_requirements,
    install_requires=requirements,
    packages=packages,
    entry_points=entry_points,
)
