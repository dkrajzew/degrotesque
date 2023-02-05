# ===================================================================
# degrotesque - A web type setter.
# Version 2.0.6
#
# Setup module
#
# (c) Daniel Krajzewicz 2020-2023
# - daniel@krajzewicz.de
# - http://www.krajzewicz.de
# - https://github.com/dkrajzew/degrotesque
# - http://www.krajzewicz.de/blog/degrotesque.php
#
# Available under the BSD license.
# ===================================================================



# --- imports -------------------------------------------------------
import setuptools


# --- definitions ---------------------------------------------------
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="degrotesque",
    version="2.0.6",
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
    },
    license='BSD',
    # add modules
    py_modules = ['degrotesque'],
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
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Localization",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Other/Nonlisted Topic",
        "Topic :: Artistic Software"
    ],
    python_requires='>=2.7, <4',
)

