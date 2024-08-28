#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
"""degrotesque - Tests for the error handling in the main method."""
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


# --- helper functions --------------------------------------------------------
def patch(string, tmp_path=None):
    if tmp_path is not None:
        tmp_path = str(tmp_path)
        string = string.replace(tmp_path, "<DIR>").replace("\\", "/")
    return string.replace("__main__.py", "degrotesque").replace("pytest", "degrotesque")


# --- test functions ----------------------------------------------------------
def test_main__unknown_option_bool(capsys, tmp_path):
    """An unknown option is given as a bool"""
    p1 = tmp_path / "hello1.html"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.html"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    try:
        degrotesque.main(["-u", str(tmp_path)])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert captured.out == ""
    assert patch(captured.err) == """usage: degrotesque [-h] [-c FILE] [--version] [-r] [-e EXTENSIONS]
                   [-E ENCODING] [-T {sgml,text,md,doxygen,python,rst}] [-B]
                   [-f {html,unicode,text}] [-s SKIP] [-w FILE] [-a ACTIONS]
                   input
degrotesque: error: unrecognized arguments: -u
"""
    assert p1.read_text() == "\"Well - that's not what I had expected.\""
    assert p2.read_text() == "\"Well - <code>that's</code> not what I had expected.\""


def test_main__unknown_option_string(capsys, tmp_path):
    """An unknown option is given as an int"""
    p1 = tmp_path / "hello1.html"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.html"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    try:
        degrotesque.main(["--foo", "bar"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert captured.out == ""
    assert patch(captured.err) == """usage: degrotesque [-h] [-c FILE] [--version] [-r] [-e EXTENSIONS]
                   [-E ENCODING] [-T {sgml,text,md,doxygen,python,rst}] [-B]
                   [-f {html,unicode,text}] [-s SKIP] [-w FILE] [-a ACTIONS]
                   input
degrotesque: error: unrecognized arguments: --foo
"""
    assert p1.read_text() == "\"Well - that's not what I had expected.\""
    assert p2.read_text() == "\"Well - <code>that's</code> not what I had expected.\""


def test_main__format__unknown(capsys, tmp_path):
    """An unknown option is given as bool"""
    p1 = tmp_path / "hello1.html"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.html"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    try:
        ret = degrotesque.main(["--format", "foo", str(tmp_path)])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert patch(captured.err) == """usage: degrotesque [-h] [-c FILE] [--version] [-r] [-e EXTENSIONS]
                   [-E ENCODING] [-T {sgml,text,md,doxygen,python,rst}] [-B]
                   [-f {html,unicode,text}] [-s SKIP] [-w FILE] [-a ACTIONS]
                   input
degrotesque: error: argument -f/--format: invalid choice: 'foo' (choose from 'html', 'unicode', 'text')
"""
    assert captured.out == ""
    assert p1.read_text() == "\"Well - that's not what I had expected.\""
    assert p2.read_text() == "\"Well - <code>that's</code> not what I had expected.\""


def test_main__filetype__unknown(capsys, tmp_path):
    """An unknown option is given as bool"""
    p1 = tmp_path / "hello1.html"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.html"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    try:
        ret = degrotesque.main(["--type", "foo", str(tmp_path)])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert patch(captured.err) == """usage: degrotesque [-h] [-c FILE] [--version] [-r] [-e EXTENSIONS]
                   [-E ENCODING] [-T {sgml,text,md,doxygen,python,rst}] [-B]
                   [-f {html,unicode,text}] [-s SKIP] [-w FILE] [-a ACTIONS]
                   input
degrotesque: error: argument -T/--type: invalid choice: 'foo' (choose from 'sgml', 'text', 'md', 'doxygen', 'python', 'rst')
"""
    assert captured.out == ""
    assert p1.read_text() == "\"Well - that's not what I had expected.\""
    assert p2.read_text() == "\"Well - <code>that's</code> not what I had expected.\""


def test_main__action__unknown(capsys, tmp_path):
    """An unknown option is given as bool"""
    p1 = tmp_path / "hello1.html"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.html"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    try:
        ret = degrotesque.main(["--actions", "foo", str(tmp_path)])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert patch(captured.err) == """usage: degrotesque [-h] [-c FILE] [--version] [-r] [-e EXTENSIONS]
                   [-E ENCODING] [-T {sgml,text,md,doxygen,python,rst}] [-B]
                   [-f {html,unicode,text}] [-s SKIP] [-w FILE] [-a ACTIONS]
                   input
degrotesque: error: argument -a/--actions: action 'foo' is not known
"""
    assert captured.out == ""
    assert p1.read_text() == "\"Well - that's not what I had expected.\""
    assert p2.read_text() == "\"Well - <code>that's</code> not what I had expected.\""


def test_main__document_broken1(capsys, tmp_path):
    """An unknown option is given as bool"""
    p1 = tmp_path / "hello1.html"
    p1.write_text("<p \"Well - that's not what I had expected.\"")
    ret = degrotesque.main([str(tmp_path)])
    captured = capsys.readouterr()
    assert captured.err == ""
    assert patch(captured.out, tmp_path) == """Processing <DIR>/hello1.html
Unclosed element at 1
"""
    assert p1.read_text() == "<p \"Well - that's not what I had expected.\""
    assert ret==4

def test_main__document_broken2(capsys, tmp_path):
    """An unknown option is given as bool"""
    p1 = tmp_path / "hello1.html"
    p1.write_text("<pre> <pre \"Well - that's not what I had expected.\"")
    ret = degrotesque.main([str(tmp_path)])
    assert ret==4
    captured = capsys.readouterr()
    assert captured.err == ""
    assert patch(captured.out, tmp_path) == """Processing <DIR>/hello1.html
Unclosed '<pre' element at position 0.
"""
    assert p1.read_text() == "<pre> <pre \"Well - that's not what I had expected.\""


def test_main__file__not_existing1(capsys, tmp_path):
    """An unknown option is given as bool"""
    p1 = tmp_path / "hello1.html"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.html"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    try:
        ret = degrotesque.main(["foo"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert patch(captured.err) == """usage: degrotesque [-h] [-c FILE] [--version] [-r] [-e EXTENSIONS]
                   [-E ENCODING] [-T {sgml,text,md,doxygen,python,rst}] [-B]
                   [-f {html,unicode,text}] [-s SKIP] [-w FILE] [-a ACTIONS]
                   input
degrotesque: error: can not process 'foo'
"""
    assert captured.out == ""
    assert p1.read_text() == "\"Well - that's not what I had expected.\""
    assert p2.read_text() == "\"Well - <code>that's</code> not what I had expected.\""
