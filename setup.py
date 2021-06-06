"""setup.py

This is the setup file for 

 degrotesque - A tiny web type setter.

(c) Daniel Krajzewicz 2020
daniel@krajzewicz.de
http://www.krajzewicz.de
http://www.krajzewicz.de/blog/degrotesque.php

Available under LGPL 3.0 or later, all rights reserved
"""

# --- imports -------------------------------------------------------
import setuptools


# --- definitions ---------------------------------------------------
with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="degrotesque",
  version="1.2",
  author="dkrajzew",
  author_email="d.krajzewicz@gmail.com",
  description="A tiny web type setter",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/dkrajzew/degrotesque",
  packages=setuptools.find_packages(),
  # see https://pypi.org/classifiers/
  classifiers=[
    "Development Status :: 5 - Production/Stable",
    "Environment :: Console",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
    "Operating System :: OS Independent",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Software Development :: Localization",
    "Topic :: Text Processing :: Markup :: HTML",
    "Topic :: Other/Nonlisted Topic",
    "Topic :: Artistic Software"
  ],
  python_requires='>=2.7, <4',
)

