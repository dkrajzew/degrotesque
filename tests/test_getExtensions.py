from __future__ import print_function
"""degrotesque.py

A tiny web type setter.

Tests teh getExtensions function.

(c) Daniel Krajzewicz 2020-2022
daniel@krajzewicz.de
http://www.krajzewicz.de
https://github.com/dkrajzew/degrotesque
http://www.krajzewicz.de/blog/degrotesque.php

Available under LGPL 3 or later, all rights reserved
"""


# --- test functions ------------------------------------------------
# ------ getExtensions ----------------------------------------------
def test_getExtensions_empty1():
    """Test getExtensions behaviour if no arguments are given (None)"""
    from degrotesque import degrotesque
    assert degrotesque.getExtensions(None) == degrotesque.extensionsDB
    

def test_getExtensions_empty2():
    """Test getExtensions behaviour if no arguments are given (empty string)"""
    from degrotesque import degrotesque
    assert degrotesque.getExtensions("") == degrotesque.extensionsDB
    

def test_getExtensions_one():
    """Test getExtensions behaviour if one argument is given"""
    from degrotesque import degrotesque
    assert degrotesque.getExtensions("foo") == ["foo"]
    

def test_getExtensions_two():
    """Test getExtensions behaviour if two arguments are given"""
    from degrotesque import degrotesque
    assert degrotesque.getExtensions("foo,bar") == ["foo", "bar"]


def test_getExtensions_strip():
    """Test getExtensions behaviour if two arguments with spaces are given"""
    from degrotesque import degrotesque
    assert degrotesque.getExtensions(" foo, bar ") == ["foo", "bar"]

