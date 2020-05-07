"""setup.py

This is the setup file for 

 degrotesque - A tiny web type setter.

(c) Daniel Krajzewicz 2020
daniel@krajzewicz.de
http://www.krajzewicz.de
http://www.krajzewicz.de/blog/degrotesque.php

Available under GPL 3.0, all rights reserved
"""

# --- imports -------------------------------------------------------
import setuptools


# --- definitions ---------------------------------------------------
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="degrotesque",
    version="0.4",
    author="dkrajzew",
    author_email="d.krajzewicz@gmail.com",
    description="A tiny web type setter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dkrajzew/degrotesque",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7, <4',
)

