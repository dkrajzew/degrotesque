from __future__ import print_function
# ===================================================================
# degrotesque - A web type setter.
# Version 2.0.
#
# Tests for the getExtensions function
#
# (c) Daniel Krajzewicz 2020-2023
# - daniel@krajzewicz.de
# - http://www.krajzewicz.de
# - https://github.com/dkrajzew/degrotesque
# - http://www.krajzewicz.de/blog/degrotesque.php
# 
# Available under the BSD license.
# ===================================================================


# --- test functions ------------------------------------------------
# ------ getExtensions ----------------------------------------------
def test_getExtensions_empty1():
    """Test getExtensions behaviour if no arguments are given (None)"""
    import degrotesque
    assert degrotesque.getExtensions(None) == degrotesque.extensionsDB
    

def test_getExtensions_empty2():
    """Test getExtensions behaviour if no arguments are given (empty string)"""
    import degrotesque
    assert degrotesque.getExtensions("") == degrotesque.extensionsDB
    

def test_getExtensions_one():
    """Test getExtensions behaviour if one argument is given"""
    import degrotesque
    assert degrotesque.getExtensions("foo") == ["foo"]
    

def test_getExtensions_two():
    """Test getExtensions behaviour if two arguments are given"""
    import degrotesque
    assert degrotesque.getExtensions("foo,bar") == ["foo", "bar"]


def test_getExtensions_strip():
    """Test getExtensions behaviour if two arguments with spaces are given"""
    import degrotesque
    assert degrotesque.getExtensions(" foo, bar ") == ["foo", "bar"]

