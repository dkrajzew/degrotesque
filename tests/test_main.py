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
sys.path.append(os.path.join(os.path.split(__file__)[0], "..", "src"))
import degrotesque



# --- helper functions --------------------------------------------------------
def patch(string):
    return string.replace("__main__.py", "degrotesque").replace("pytest", "degrotesque").replace("optional arguments", "options")



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
    assert patch(captured.err) == """usage: degrotesque [-h] [-c FILE] [--version] [-r] [-e EXTENSIONS]
                   [-E ENCODING] [-t {sgml,text,md,doxygen,python,rst}] [-B]
                   [-f {html,unicode,char}] [-s SKIP] [-a ACTIONS] [-w FILE]
                   input
degrotesque: error: the following arguments are required: input
"""
    assert patch(captured.out) == ""


def test_main_empty2(capsys):
    """Test behaviour if no arguments are given"""
    try:
        ret = degrotesque.main()
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert patch(captured.err) == """usage: degrotesque [-h] [-c FILE] [--version] [-r] [-e EXTENSIONS]
                   [-E ENCODING] [-t {sgml,text,md,doxygen,python,rst}] [-B]
                   [-f {html,unicode,char}] [-s SKIP] [-a ACTIONS] [-w FILE]
                   input
degrotesque: error: the following arguments are required: input
"""
    assert patch(captured.out) == ""


def test_main_help(capsys):
    """Test behaviour when help is wished"""
    try:
        degrotesque.main(["--help"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert patch(captured.out) == """usage: degrotesque [-h] [-c FILE] [--version] [-r] [-e EXTENSIONS]
                   [-E ENCODING] [-t {sgml,text,md,doxygen,python,rst}] [-B]
                   [-f {html,unicode,char}] [-s SKIP] [-a ACTIONS] [-w FILE]
                   input

A type setter that exchanges ascii letters by their typographic counterparts

positional arguments:
  input

options:
  -h, --help            show this help message and exit
  -c FILE, --config FILE
                        Reads the named configuration file
  --version             show program's version number and exit
  -r, --recursive       Whether a given path shall be processed recursively
  -e EXTENSIONS, --extensions EXTENSIONS
                        Defines the extensions of files to process
  -E ENCODING, --encoding ENCODING
                        File encoding (default: 'utf-8')
  -t {sgml,text,md,doxygen,python,rst}, --type {sgml,text,md,doxygen,python,rst}
                        Name the file type, one of ['sgml', 'text', 'md',
                        'doxygen', 'python', 'rst']
  -B, --no-backup       Whether no backup shall be generated
  -f {html,unicode,char}, --format {html,unicode,char}
                        Defines the format of the replacements ['html',
                        'unicode', 'char']
  -s SKIP, --skip SKIP  Defines the elements which contents shall not be
                        changed
  -a ACTIONS, --actions ACTIONS
                        Defines the actions to perform
  -w FILE, --write-config FILE
                        Writes the current settings to the named configuration
                        file

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
    assert patch(captured.out) == """degrotesque 3.0.0
"""
    assert patch(captured.err) == ""


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
    """Test behaviour with given extensions"""
    p1 = tmp_path / "hello1.html"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.html"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    degrotesque.main(["-f", "html", str(tmp_path)])
    assert p1.read_text() == "&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;"
    assert p2.read_text() == "&ldquo;Well &mdash; <code>that's</code> not what I had expected.&rdquo;"


def test_main_run1_html2html_namedtype(capsys, tmp_path):
    """Test behaviour within given file types"""
    p1 = tmp_path / "hello1.html"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.html"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    degrotesque.main(["--type", "sgml", "-f", "html", str(tmp_path)])
    assert p1.read_text() == "&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;"
    assert p2.read_text() == "&ldquo;Well &mdash; <code>that's</code> not what I had expected.&rdquo;"


def test_main_run1_html2html_sgmlguess1(capsys, tmp_path):
    """Tests HTML gueassing"""
    p1 = tmp_path / "hello1.xxx"
    p1.write_text("<!DOCTYPE>\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.xxx"
    p2.write_text("<!DOCTYPE>\"Well - <code>that's</code> not what I had expected.\"")
    degrotesque.main(["-f", "html", str(tmp_path)])
    assert p1.read_text() == "<!DOCTYPE>&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;"
    assert p2.read_text() == "<!DOCTYPE>&ldquo;Well &mdash; <code>that's</code> not what I had expected.&rdquo;"

def test_main_run1_html2html_sgmlguess2(capsys, tmp_path):
    """Tests HTML gueassing"""
    p1 = tmp_path / "hello1.xxx"
    p1.write_text("<!doctype>\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.xxx"
    p2.write_text("<!doctype>\"Well - <code>that's</code> not what I had expected.\"")
    degrotesque.main(["-f", "html", str(tmp_path)])
    assert p1.read_text() == "<!doctype>&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;"
    assert p2.read_text() == "<!doctype>&ldquo;Well &mdash; <code>that's</code> not what I had expected.&rdquo;"

def test_main_run1_html2html_sgmlguess3(capsys, tmp_path):
    """Tests HTML gueassing"""
    p1 = tmp_path / "hello1.xxx"
    p1.write_text("<?xml>\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.xxx"
    p2.write_text("<?xml>\"Well - <code>that's</code> not what I had expected.\"")
    degrotesque.main(["-f", "html", str(tmp_path)])
    assert p1.read_text() == "<?xml>&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;"
    assert p2.read_text() == "<?xml>&ldquo;Well &mdash; <code>that's</code> not what I had expected.&rdquo;"

def test_main_run1_html2html_sgmlguess4(capsys, tmp_path):
    """Tests HTML gueassing"""
    p1 = tmp_path / "hello1.xxx"
    p1.write_text("<x>\"Well - that's not what I had expected.\"</x>")
    p2 = tmp_path / "hello2.xxx"
    p2.write_text("<x>\"Well - <code>that's</code> not what I had expected.\"</x>")
    degrotesque.main(["-f", "html", str(tmp_path)])
    assert p1.read_text() == "<x>&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;</x>"
    assert p2.read_text() == "<x>&ldquo;Well &mdash; <code>that's</code> not what I had expected.&rdquo;</x>"

def test_main_run1_html2html_sgmlguess5(capsys, tmp_path):
    """Tests HTML gueassing"""
    p1 = tmp_path / "hello1.xxx"
    p1.write_text("<x>\"Well - that's not what I had expected.\"</x>\n")
    p2 = tmp_path / "hello2.xxx"
    p2.write_text("<x>\"Well - <code>that's</code> not what I had expected.\"</x>\n")
    degrotesque.main(["-f", "html", str(tmp_path)])
    assert p1.read_text() == "<x>&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;</x>\n"
    assert p2.read_text() == "<x>&ldquo;Well &mdash; <code>that's</code> not what I had expected.&rdquo;</x>\n"

def test_main_run1_html2html_sgmlguess_nosgml(capsys, tmp_path):
    """Tests HTML gueassing"""
    p1 = tmp_path / "hello1.xxx"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.xxx"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    degrotesque.main(["-f", "html", str(tmp_path)])
    assert p1.read_text() == "&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;"
    assert p2.read_text() == "&ldquo;Well &mdash; <code>that&apos;s</code> not what I had expected.&rdquo;"


def test_main_run1_md2html(capsys, tmp_path):
    """Tests processing of md files"""
    p1 = tmp_path / "hello1.md"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.md"
    p2.write_text("\"Well - `that's` not what I had expected.\"")
    degrotesque.main(["-f", "html", str(tmp_path)])
    assert p1.read_text() == "&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;"
    assert p2.read_text() == "&ldquo;Well &mdash; `that's` not what I had expected.&rdquo;"


def test_main_run1_md2html_namedtype(capsys, tmp_path):
    """Tests processing of md files"""
    p1 = tmp_path / "hello1.md"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.md"
    p2.write_text("\"Well - `that's` not what I had expected.\"")
    degrotesque.main(["--type", "md", "-f", "html", str(tmp_path)])
    assert p1.read_text() == "&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;"
    assert p2.read_text() == "&ldquo;Well &mdash; `that's` not what I had expected.&rdquo;"
