#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
"""degrotesque - Tests for the helper.get_files function."""
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
import helper


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


# typed files (extension is given)
def test_get_typed_files_one(tmp_path):
    """One file is given (explicit)"""
    p = tmp_path / "hello.html"
    p.write_text("Hallo <b>Mama</b>")
    files = helper.get_files(tmp_path / "hello.html", False, ["html"])
    check_files(["hello.html"], files, tmp_path)

def test_get_typed_files_multiple1(tmp_path):
    """Two files are given (explicit)"""
    p = tmp_path / "hello1.html"
    p.write_text("Hallo <b>Mama</b>")
    p = tmp_path / "hello2.html"
    p.write_text("Hallo <b>Mama</b>")
    files = helper.get_files(tmp_path, False, ["html"])
    check_files(["hello1.html", "hello2.html"], files, tmp_path)

def test_get_typed_files_multiple2(tmp_path):
    """Two files exist but only .html-files shall be processed"""
    p = tmp_path / "hello1.html"
    p.write_text("Hallo <b>Mama</b>")
    p = tmp_path / "hello2.txt"
    p.write_text("Hallo <b>Mama</b>")
    files = helper.get_files(tmp_path, False, ["html"])
    check_files(["hello1.html"], files, tmp_path)

def test_get_typed_files_multiple_recursive1(tmp_path):
    """Recusrsive folder structure with recursion disabled"""
    p = tmp_path / "hello1.html"
    p.write_text("Hallo <b>Mama</b>")
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello2.html"
    p.write_text("Hallo <b>Mama</b>")
    files = helper.get_files(tmp_path, False, ["html"])
    check_files(["hello1.html"], files, tmp_path)

def test_get_typed_files_multiple_recursive2(tmp_path):
    """Recusrsive folder structure with recursion enabled"""
    p = tmp_path / "hello1.html"
    p.write_text("Hallo <b>Mama</b>")
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello2.html"
    p.write_text("Hallo <b>Mama</b>")
    files = helper.get_files(tmp_path, True, ["html"])
    check_files(["hello1.html", "sub/hello2.html"], files, tmp_path)

def test_get_typed_files_multiple_recursive3(tmp_path):
    """Recusrsive folder structure with recursion enabled, HTML files only"""
    p = tmp_path / "hello1.html"
    p.write_text("Hallo <b>Mama</b>")
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello2.html"
    p.write_text("Hallo <b>Mama</b>")
    p = d / "hello3.txt"
    p.write_text("Hallo <b>Mama</b>")
    files = helper.get_files(tmp_path, True, ["html"])
    check_files(["hello1.html", "sub/hello2.html"], files, tmp_path)



# untyped files (extension is not given)
def test_get_untyped_files_one(tmp_path):
    """One file is given"""
    p = tmp_path / "hello.html"
    p.write_text("Hallo <b>Mama</b>")
    files = helper.get_files(tmp_path / "hello.html", False, None)
    check_files(["hello.html"], files, tmp_path)

def test_get_untyped_files_multiple1(tmp_path):
    """Two files are given"""
    p = tmp_path / "hello1.html"
    p.write_text("Hallo <b>Mama</b>")
    p = tmp_path / "hello2.html"
    p.write_text("Hallo <b>Mama</b>")
    files = helper.get_files(tmp_path, False, None)
    check_files(["hello1.html", "hello2.html"], files, tmp_path)

def test_get_untyped_files_multiple2(tmp_path):
    """Two files are given"""
    p = tmp_path / "hello1.html"
    p.write_text("Hallo <b>Mama</b>")
    p = tmp_path / "hello2.txt"
    p.write_text("Hallo <b>Mama</b>")
    files = helper.get_files(tmp_path, False, None)
    check_files(["hello1.html", "hello2.txt"], files, tmp_path)

def test_get_untyped_files_multiple_recursive1(tmp_path):
    """Recusrsive folder structure with recursion disabled"""
    p = tmp_path / "hello1.html"
    p.write_text("Hallo <b>Mama</b>")
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello2.html"
    p.write_text("Hallo <b>Mama</b>")
    files = helper.get_files(tmp_path, False, None)
    check_files(["hello1.html"], files, tmp_path)

def test_get_untyped_files_multiple_recursive2(tmp_path):
    """Recusrsive folder structure with recursion enabled"""
    p = tmp_path / "hello1.html"
    p.write_text("Hallo <b>Mama</b>")
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello2.html"
    p.write_text("Hallo <b>Mama</b>")
    files = helper.get_files(tmp_path, True, None)
    check_files(["hello1.html", "sub/hello2.html"], files, tmp_path)

def test_get_untyped_files_multiple_recursive3(tmp_path):
    """Recusrsive folder structure with recursion enabled"""
    p = tmp_path / "hello1.html"
    p.write_text("Hallo <b>Mama</b>")
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello2.html"
    p.write_text("Hallo <b>Mama</b>")
    p = d / "hello3.txt"
    p.write_text("Hallo <b>Mama</b>")
    files = helper.get_files(tmp_path, True, None)
    check_files(["hello1.html", "sub/hello2.html", "sub/hello3.txt"], files, tmp_path)



# error cases
def test_get_files_not_existing(tmp_path):
    """Named file does not exist"""
    try:
        files = helper.get_files(tmp_path / "hello.html", False, None)
    except ValueError as e:
        assert type(e)==type(ValueError())
        assert str(e).replace(str(tmp_path), "<DIR>").replace("\\", "/")=="can not process '<DIR>/hello.html'"
