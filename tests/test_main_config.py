#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
"""degrotesque - Tests for using configurations."""
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
    return string.replace("__main__.py", "degrotesque").replace("pytest", "degrotesque").replace("optional arguments", "options")



# --- test functions ----------------------------------------------------------
def test_main_config_read1(capsys, tmp_path):
    """Reads a config (HTML parsing)"""
    p1 = tmp_path / "hello1.html"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.html"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    base_dir = os.path.split(__file__)[0]
    ret = degrotesque.main(["-c", os.path.join(base_dir, "format_html.cfg"), str(tmp_path)])
    assert ret==0
    assert p1.read_text() == "&#8220;Well &#8212; that&#39;s not what I had expected.&#8221;"
    assert p2.read_text() == "&#8220;Well &#8212; <code>that's</code> not what I had expected.&#8221;"

def test_main_config_read2(capsys, tmp_path):
    """Reads a config (text parsing)"""
    p1 = tmp_path / "hello1.html"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.html"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    base_dir = os.path.split(__file__)[0]
    ret = degrotesque.main(["-c", os.path.join(base_dir, "format_text.cfg"), str(tmp_path)])
    assert ret==0
    assert p1.read_text() == "&#8220;Well &#8212; that&#39;s not what I had expected.&#8221;"
    assert p2.read_text() == "&#8220;Well &#8212; <code>that&#39;s</code> not what I had expected.&#8221;"



def test_main_config_write1(capsys, tmp_path):
    """Writes a config"""
    p1 = tmp_path / "hello1.html"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.html"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    pc = tmp_path / "out_html.cfg"
    base_dir = os.path.split(__file__)[0]
    ret = degrotesque.main(["--type", "sgml", "-w", str(pc), str(tmp_path)])
    assert ret==0
    assert p1.read_text() == "&#8220;Well &#8212; that&#39;s not what I had expected.&#8221;"
    assert p2.read_text() == "&#8220;Well &#8212; <code>that's</code> not what I had expected.&#8221;"
    assert patch(pc.read_text(), tmp_path) == """[degrotesque]
input=<DIR>
recursive=False
encoding=utf-8
type=sgml
no_backup=False
format=unicode
"""






