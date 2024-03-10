#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
"""degrotesque - Tests for determining the file type."""
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
from degrotesque import degrotesque


# --- test functions ----------------------------------------------------------
def test_filetype__two_html(capsys, tmp_path):
    """Whether two HTML files are processed"""
    p1 = tmp_path / "hello1.html"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.html"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    degrotesque.main(["-i", tmp_path])
    #captured = capsys.readouterr()
    #assert captured.out == ""
    #assert captured.err == ""
    assert p1.read_text() == "&#8220;Well &#8212; that&#39;s not what I had expected.&#8221;"
    assert p2.read_text() == "&#8220;Well &#8212; <code>that's</code> not what I had expected.&#8221;"


def test_filetype__two_text(capsys, tmp_path):
    """Whether two text files are processed
    
    The second file is recognized as HTML due to it's contents
    """
    p1 = tmp_path / "hello1.txt"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.txt"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    degrotesque.main(["-i", tmp_path])
    #captured = capsys.readouterr()
    #assert captured.out == ""
    #assert captured.err == ""
    assert p1.read_text() == "&#8220;Well &#8212; that&#39;s not what I had expected.&#8221;"
    assert p2.read_text() == "&#8220;Well &#8212; <code>that's</code> not what I had expected.&#8221;"


def test_filetype__two_text_explicit(capsys, tmp_path):
    """Whether two text files are processed
    
    The second file is recognized as HTML due to it's contents
    """
    p1 = tmp_path / "hello1.txt"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.txt"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    degrotesque.main(["-i", tmp_path, "--text"])
    #captured = capsys.readouterr()
    #assert captured.out == ""
    #assert captured.err == ""
    assert p1.read_text() == "&#8220;Well &#8212; that&#39;s not what I had expected.&#8221;"
    assert p2.read_text() == "&#8220;Well &#8212; <code>that&#39;s</code> not what I had expected.&#8221;"
