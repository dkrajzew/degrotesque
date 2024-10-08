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
import sys
import os
sys.path.append(os.path.join(os.path.split(__file__)[0], "..", "src"))
import degrotesque


# --- test functions ----------------------------------------------------------
def test_filetype__two_html(capsys, tmp_path):
    """Two HTML files (by extension)"""
    p1 = tmp_path / "hello1.html"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.html"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    degrotesque.main([str(tmp_path)])
    assert p1.read_text() == "&#8220;Well &#8212; that&#39;s not what I had expected.&#8221;"
    assert p2.read_text() == "&#8220;Well &#8212; <code>that's</code> not what I had expected.&#8221;"


def test_filetype__two_html_explicit(capsys, tmp_path):
    """Two HTML files (explicit)"""
    p1 = tmp_path / "hello1.html"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.html"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    degrotesque.main(["--type", "sgml", str(tmp_path)])
    assert p1.read_text() == "&#8220;Well &#8212; that&#39;s not what I had expected.&#8221;"
    assert p2.read_text() == "&#8220;Well &#8212; <code>that's</code> not what I had expected.&#8221;"



def test_filetype__two_text(capsys, tmp_path):
    """Two text files (by extension)"""
    p1 = tmp_path / "hello1.txt"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.txt"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    degrotesque.main([str(tmp_path)])
    assert p1.read_text() == "&#8220;Well &#8212; that&#39;s not what I had expected.&#8221;"
    assert p2.read_text() == "&#8220;Well &#8212; <code>that&#39;s</code> not what I had expected.&#8221;"


def test_filetype__two_text_explicit(capsys, tmp_path):
    """Two text files (explicit)"""
    p1 = tmp_path / "hello1.txt"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.txt"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    degrotesque.main(["--type", "text", str(tmp_path)])
    assert p1.read_text() == "&#8220;Well &#8212; that&#39;s not what I had expected.&#8221;"
    assert p2.read_text() == "&#8220;Well &#8212; <code>that&#39;s</code> not what I had expected.&#8221;"



def test_filetype__two_md(capsys, tmp_path):
    """Two md files (by extension)"""
    p1 = tmp_path / "hello1.md"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.md"
    p2.write_text("\"Well - ```that's``` not what I had expected.\"")
    degrotesque.main([str(tmp_path)])
    assert p1.read_text() == "&#8220;Well &#8212; that&#39;s not what I had expected.&#8221;"
    assert p2.read_text() == "&#8220;Well &#8212; ```that's``` not what I had expected.&#8221;"


def test_filetype__two_md_explicit(capsys, tmp_path):
    """Two md files (explicit)"""
    p1 = tmp_path / "hello1.txt"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.txt"
    p2.write_text("\"Well - ```that's``` not what I had expected.\"")
    degrotesque.main(["--type", "md", str(tmp_path)])
    assert p1.read_text() == "&#8220;Well &#8212; that&#39;s not what I had expected.&#8221;"
    assert p2.read_text() == "&#8220;Well &#8212; ```that's``` not what I had expected.&#8221;"



def test_filetype__three_python(capsys, tmp_path):
    """Three Python files (by extension)"""
    p1 = tmp_path / "hello1.py"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.py"
    p2.write_text("\"Well - \"\"\"that's\"\"\" not what I had expected.\"")
    p3 = tmp_path / "hello3.py"
    p3.write_text("\"\"\"Well - that's not what I had expected.\"\"\"")
    degrotesque.main([str(tmp_path)])
    assert p1.read_text() == "\"Well - that's not what I had expected.\""
    assert p2.read_text() == "\"Well - \"\"\"that&#39;s\"\"\" not what I had expected.\""
    assert p3.read_text() == "\"\"\"Well &#8212; that&#39;s not what I had expected.\"\"\""


def test_filetype__three_python_explicit(capsys, tmp_path):
    """Three Python files (explicit)"""
    p1 = tmp_path / "hello1.txt"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.txt"
    p2.write_text("\"Well - \"\"\"that's\"\"\" not what I had expected.\"")
    p3 = tmp_path / "hello3.txt"
    p3.write_text("\"\"\"Well - that's not what I had expected.\"\"\"")
    degrotesque.main(["--type", "python", str(tmp_path)])
    assert p1.read_text() == "\"Well - that's not what I had expected.\""
    assert p2.read_text() == "\"Well - \"\"\"that&#39;s\"\"\" not what I had expected.\""
    assert p3.read_text() == "\"\"\"Well &#8212; that&#39;s not what I had expected.\"\"\""



def test_filetype__three_doxygen(capsys, tmp_path):
    """Three Java files (by extension)"""
    p1 = tmp_path / "hello1.java"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.java"
    p2.write_text("\"Well - /**that's*/ not what I had expected.\"")
    p3 = tmp_path / "hello3.java"
    p3.write_text("/**Well - that's not what I had expected.*/")
    degrotesque.main([str(tmp_path)])
    assert p1.read_text() == "\"Well - that's not what I had expected.\""
    assert p2.read_text() == "\"Well - /**that&#39;s*/ not what I had expected.\""
    assert p3.read_text() == "/**Well &#8212; that&#39;s not what I had expected.*/"


def test_filetype__three_doxygen_explicit(capsys, tmp_path):
    """Three Java files (explicit)"""
    p1 = tmp_path / "hello1.txt"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.txt"
    p2.write_text("\"Well - /**that's*/ not what I had expected.\"")
    p3 = tmp_path / "hello3.txt"
    p3.write_text("/**Well - that's not what I had expected.*/")
    degrotesque.main(["--type", "doxygen", str(tmp_path)])
    assert p1.read_text() == "\"Well - that's not what I had expected.\""
    assert p2.read_text() == "\"Well - /**that&#39;s*/ not what I had expected.\""
    assert p3.read_text() == "/**Well &#8212; that&#39;s not what I had expected.*/"



def test_filetype__three_rst(capsys, tmp_path):
    """Three rst files (by extension)"""
    p1 = tmp_path / "hello1.rst"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.rst"
    p2.write_text("\"Well - ``that's`` not what I had expected.\"")
    p3 = tmp_path / "hello3.rst"
    p3.write_text("``\"Well - that's not what I had expected.\"``")
    degrotesque.main([str(tmp_path)])
    assert p1.read_text() == "&#8220;Well &#8212; that&#39;s not what I had expected.&#8221;"
    assert p2.read_text() == "&#8220;Well &#8212; ``that's`` not what I had expected.&#8221;"
    assert p3.read_text() == "``\"Well - that's not what I had expected.\"``"


def test_filetype__three_rst_explicit(capsys, tmp_path):
    """Three rst files (explicit)"""
    p1 = tmp_path / "hello1.txt"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.txt"
    p2.write_text("\"Well - ``that's`` not what I had expected.\"")
    p3 = tmp_path / "hello3.txt"
    p3.write_text("``\"Well - that's not what I had expected.\"``")
    degrotesque.main(["--type", "rst", str(tmp_path)])
    assert p1.read_text() == "&#8220;Well &#8212; that&#39;s not what I had expected.&#8221;"
    assert p2.read_text() == "&#8220;Well &#8212; ``that's`` not what I had expected.&#8221;"
    assert p3.read_text() == "``\"Well - that's not what I had expected.\"``"
