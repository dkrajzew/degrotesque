#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
# =============================================================================
"""degrotesque - A web type setter."""
# =============================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2020-2024, Daniel Krajzewicz"
__credits__    = ["Daniel Krajzewicz"]
__license__    = "BSD"
__version__    = "3.0.0"
__maintainer__ = "Daniel Krajzewicz"
__email__      = "daniel@krajzewicz.de"
__status__     = "Production"
# =============================================================================
# - https://github.com/dkrajzew/degrotesque
# - http://www.krajzewicz.de/docs/degrotesque/index.html
# - http://www.krajzewicz.de
# =============================================================================


# --- imports -----------------------------------------------------------------
import setuptools


# --- definitions -------------------------------------------------------------
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="degrotesque",
    version="3.0.0",
    author="dkrajzew",
    author_email="d.krajzewicz@gmail.com",
    description="A web type setter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://degrotesque.readthedocs.org/',
    download_url='http://pypi.python.org/pypi/degrotesque',
    project_urls={
        'Documentation': 'https://degrotesque.readthedocs.io/',
        'Source': 'https://github.com/dkrajzew/degrotesque',
        'Tracker': 'https://github.com/dkrajzew/degrotesque/issues',
        'Discussions': 'https://github.com/dkrajzew/degrotesque/discussions',
    },
    license='BSD',
    # add modules
    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': [
            'degrotesque = degrotesque:main'
        ]
    },
    # see https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Telecommunications Industry",
        "Topic :: Documentation",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Localization",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Other/Nonlisted Topic",
        "Topic :: Artistic Software"
    ],
    python_requires='>=2.7, <4',
)

