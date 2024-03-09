#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
"""Tests for the get_extensions function."""
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


# --- test functions ----------------------------------------------------------
def test_get_extensions_empty1():
    """Test get_extensions behaviour if no arguments are given (None)"""
    import degrotesque
    assert degrotesque.get_extensions(None) == None


def test_get_extensions_empty2():
    """Test get_extensions behaviour if no arguments are given (empty string)"""
    import degrotesque
    assert degrotesque.get_extensions("") == None


def test_get_extensions_one():
    """Test get_extensions behaviour if one argument is given"""
    import degrotesque
    assert degrotesque.get_extensions("foo") == ["foo"]


def test_get_extensions_two():
    """Test get_extensions behaviour if two arguments are given"""
    import degrotesque
    assert degrotesque.get_extensions("foo,bar") == ["foo", "bar"]


def test_get_extensions_strip():
    """Test get_extensions behaviour if two arguments with spaces are given"""
    import degrotesque
    assert degrotesque.get_extensions(" foo, bar ") == ["foo", "bar"]


def test_get_extensions_asterisk():
    """Test get_extensions behaviour if one of the given items is an asterisk"""
    import degrotesque
    assert degrotesque.get_extensions(" foo, * ") == None
