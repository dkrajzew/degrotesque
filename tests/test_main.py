#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
"""degrotesque - Tests for the main method."""
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
sys.path.append(os.path.join(os.path.split(__file__)[0], "..", "degrotesque"))
import degrotesque


# --- test functions ----------------------------------------------------------
def test_main_empty1(capsys):
    """Test behaviour if no arguments are given"""
    try:
        ret = degrotesque.main([])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert captured.err.replace("__main__.py", "degrotesque.py") == """usage: degrotesque [-h] [--version] [-r] [-e EXTENSIONS] [-E ENCODING] [-H]
                   [-T] [-M] [-D] [-P] [-B] [-f FORMAT] [-s SKIP] [-a ACTIONS]
                   input
degrotesque: error: the following arguments are required: input
"""
    assert captured.out.replace("__main__.py", "degrotesque.py") == ""


def test_main_empty2(capsys):
    """Test behaviour if no arguments are given"""
    try:
        ret = degrotesque.main()
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert captured.err.replace("__main__.py", "degrotesque.py") == """usage: degrotesque [-h] [--version] [-r] [-e EXTENSIONS] [-E ENCODING] [-H]
                   [-T] [-M] [-D] [-P] [-B] [-f FORMAT] [-s SKIP] [-a ACTIONS]
                   input
degrotesque: error: the following arguments are required: input
"""
    assert captured.out.replace("__main__.py", "degrotesque.py") == ""


def test_main_help(capsys):
    """Test behaviour when help is wished"""
    try:
        degrotesque.main(["--help"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert captured.out.replace("__main__.py", "degrotesque.py") == """usage: degrotesque [-h] [--version] [-r] [-e EXTENSIONS] [-E ENCODING] [-H]
                   [-T] [-M] [-D] [-P] [-B] [-f FORMAT] [-s SKIP] [-a ACTIONS]
                   input

A weg type setter; Exchanges simple ascii letters by their typographic
counterparts

positional arguments:
  input

options:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -r, --recursive       Whether a given path shall be processed recursively
  -e EXTENSIONS, --extensions EXTENSIONS
                        Defines the extensions of files to process
  -E ENCODING, --encoding ENCODING
                        File encoding (default: 'utf-8')
  -H, --html            Files are HTML/XML-derivatives
  -T, --text            Files are plain text files
  -M, --markdown        Files are markdown files
  -D, --doxygen         Files are doxygen files
  -P, --python          Files are Python files
  -B, --no-backup       Whether no backup shall be generated
  -f FORMAT, --format FORMAT
                        Defines the format of the replacements ['html',
                        'unicode', 'text']
  -s SKIP, --skip SKIP  Defines the elements which contents shall not be
                        changed
  -a ACTIONS, --actions ACTIONS
                        Defines the actions to perform

(c) Daniel Krajzewicz 2020-2024
"""
    assert captured.err == ""


def test_main_version(capsys):
    """Test behaviour when version information is wished"""
    try:
        degrotesque.main(["--version"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert captured.out.replace("__main__.py", "degrotesque") == """degrotesque 3.0.0
"""
    assert captured.err == ""


def test_main_run1(capsys, tmp_path):
    """Test behaviour on plain usage"""
    p1 = tmp_path / "hello1.html"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.html"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    degrotesque.main([str(tmp_path)])
    assert p1.read_text() == "&#8220;Well &#8212; that&#39;s not what I had expected.&#8221;"
    assert p2.read_text() == "&#8220;Well &#8212; <code>that's</code> not what I had expected.&#8221;"


def test_main_run1_html2html(capsys, tmp_path):
    """Test behaviour on plain usage"""
    p1 = tmp_path / "hello1.html"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.html"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    degrotesque.main(["-f", "html", str(tmp_path)])
    assert p1.read_text() == "&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;"
    assert p2.read_text() == "&ldquo;Well &mdash; <code>that's</code> not what I had expected.&rdquo;"


def test_main_run1_html2html_namedtype(capsys, tmp_path):
    """Test behaviour on plain usage"""
    p1 = tmp_path / "hello1.html"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.html"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    degrotesque.main(["--html", "-f", "html", str(tmp_path)])
    assert p1.read_text() == "&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;"
    assert p2.read_text() == "&ldquo;Well &mdash; <code>that's</code> not what I had expected.&rdquo;"


def test_main_run1_html2html_sgmlguess(capsys, tmp_path):
    """Test behaviour on plain usage"""
    p1 = tmp_path / "hello1.xxx"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.xxx"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    degrotesque.main(["-f", "html", str(tmp_path)])
    assert p1.read_text() == "&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;"
    assert p2.read_text() == "&ldquo;Well &mdash; <code>that's</code> not what I had expected.&rdquo;"


def test_main_run1_md2html(capsys, tmp_path):
    """Test behaviour on plain usage"""
    p1 = tmp_path / "hello1.md"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.md"
    p2.write_text("\"Well - `that's` not what I had expected.\"")
    degrotesque.main(["-f", "html", str(tmp_path)])
    assert p1.read_text() == "&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;"
    assert p2.read_text() == "&ldquo;Well &mdash; `that's` not what I had expected.&rdquo;"


def test_main_run1_md2html_namedtype(capsys, tmp_path):
    """Test behaviour on plain usage"""
    p1 = tmp_path / "hello1.md"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.md"
    p2.write_text("\"Well - `that's` not what I had expected.\"")
    degrotesque.main(["--markdown", "-f", "html", str(tmp_path)])
    assert p1.read_text() == "&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;"
    assert p2.read_text() == "&ldquo;Well &mdash; `that's` not what I had expected.&rdquo;"


def test_main_error_multiplemarkers(capsys, tmp_path):
    """Test behaviour on plain usage"""
    p1 = tmp_path / "hello1.md"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.md"
    p2.write_text("\"Well - `that's` not what I had expected.\"")
    ret = degrotesque.main(["--html", "--markdown", str(tmp_path)])
    assert ret==2
    captured = capsys.readouterr()
    assert captured.err.replace("__main__.py", "degrotesque") == """usage: degrotesque [-h] [--version] [-r] [-e EXTENSIONS] [-E ENCODING] [-H]
                   [-T] [-M] [-D] [-P] [-B] [-f FORMAT] [-s SKIP] [-a ACTIONS]
                   input
degrotesque: error: only one of the options '--html', '--markdown', '--doxygen', '--python', and '--text' can be set.
"""


