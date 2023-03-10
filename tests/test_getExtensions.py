from __future__ import print_function
# ===================================================================
# degrotesque - A web type setter.
#
# Tests for the getExtensions function
#
# (c) Daniel Krajzewicz 2020-2023
# daniel@krajzewicz.de
# - https://github.com/dkrajzew/degrotesque
# - http://www.krajzewicz.de/docs/degrotesque/index.html
# - http://www.krajzewicz.de
#
# Available under the BSD license.
# ===================================================================


# --- test functions ------------------------------------------------
# ------ getExtensions ----------------------------------------------
def test_getExtensions_empty1():
    """Test getExtensions behaviour if no arguments are given (None)"""
    import degrotesque
    assert degrotesque.getExtensions(None) == None


def test_getExtensions_empty2():
    """Test getExtensions behaviour if no arguments are given (empty string)"""
    import degrotesque
    assert degrotesque.getExtensions("") == None


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


def test_getExtensions_asterisk():
    """Test getExtensions behaviour if one of the given items is an asterisk"""
    import degrotesque
    assert degrotesque.getExtensions(" foo, * ") == None

