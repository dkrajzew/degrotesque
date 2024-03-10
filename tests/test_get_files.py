#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
"""degrotesque - Tests for the get_files function."""
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
def check_files(wanted, got, path):
    got2 = []
    for f in got:
        f = str(f).replace(str(path), "")
        f = f.replace('\\', '/')
        if f[0]=='/':
            f = f[1:]
        got2.append(f)
    assert wanted==got2

def test_get_files_one(tmp_path):
    """Test get_files behaviour if one file is given"""
    p = tmp_path / "hello.html"
    p.write_text("Hallo <b>Mama</b>")
    files = degrotesque.get_files(tmp_path / "hello.html", False, ["html"])
    check_files(["hello.html"], files, tmp_path)

def test_get_files_multiple1(tmp_path):
    """Test get_files behaviour if two files is given"""
    p = tmp_path / "hello1.html"
    p.write_text("Hallo <b>Mama</b>")
    p = tmp_path / "hello2.html"
    p.write_text("Hallo <b>Mama</b>")
    files = degrotesque.get_files(tmp_path, False, ["html"])
    check_files(["hello1.html", "hello2.html"], files, tmp_path)

def test_get_files_multiple2(tmp_path):
    """Test get_files behaviour if two files exist but only .html-files shall be processed"""
    p = tmp_path / "hello1.html"
    p.write_text("Hallo <b>Mama</b>")
    p = tmp_path / "hello2.txt"
    p.write_text("Hallo <b>Mama</b>")
    files = degrotesque.get_files(tmp_path, False, ["html"])
    check_files(["hello1.html"], files, tmp_path)

def test_get_files_multiple_recursive1(tmp_path):
    """Tests recusrsive folder structure with recursion disabled"""
    p = tmp_path / "hello1.html"
    p.write_text("Hallo <b>Mama</b>")
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello2.html"
    p.write_text("Hallo <b>Mama</b>")
    files = degrotesque.get_files(tmp_path, False, ["html"])
    check_files(["hello1.html"], files, tmp_path)

def test_get_files_multiple_recursive2(tmp_path):
    """Tests recusrsive folder structure with recursion enabled"""
    p = tmp_path / "hello1.html"
    p.write_text("Hallo <b>Mama</b>")
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello2.html"
    p.write_text("Hallo <b>Mama</b>")
    files = degrotesque.get_files(tmp_path, True, ["html"])
    check_files(["hello1.html", "sub/hello2.html"], files, tmp_path)


