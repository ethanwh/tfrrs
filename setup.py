#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
        name="tfrrs",
        author="Ethan Homan",
        author_email="ewhoman@bu.edu",
        version="0.0.2",
        description="Fetches meet results from tfrrs.org and writes them to a csv file",
        url="https://github.com/ewhoman/tfrrs",
        license="MIT",
        packages =find_packages(), 
        install_requires = ['requests','beautifulsoup4'],
        entry_points = {'console_scripts' : ['tfrrs = tfrrs:cli.cli']}
        )

