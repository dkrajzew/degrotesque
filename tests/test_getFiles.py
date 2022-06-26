from __future__ import print_function
"""degrotesque.py

A tiny web type setter.

Tests for the getFiles function.

(c) Daniel Krajzewicz 2020-2022
daniel@krajzewicz.de
http://www.krajzewicz.de
https://github.com/dkrajzew/degrotesque
http://www.krajzewicz.de/blog/degrotesque.php

Available under EPL 2.0 or later, all rights reserved
"""
# --- test functions ------------------------------------------------
# ------ getFiles ---------------------------------------------------
def checkFiles(wanted, got, path):
    got2 = []
    for f in got:
        f = str(f).replace(str(path), "")
        f = f.replace('\\', '/')
        if f[0]=='/':
            f = f[1:]
        got2.append(f)
    assert wanted==got2        

def test_getFiles_one(tmp_path):
    """Test getExtensions behaviour if no arguments are given (None)"""
    from degrotesque import degrotesque
    p = tmp_path / "hello.html"
    p.write_text("Hallo <b>Mama</b>")
    files = degrotesque.getFiles(tmp_path / "hello.html", False, ["html"])
    checkFiles(["hello.html"], files, tmp_path) 
    
def test_getFiles_multiple1(tmp_path):
    """Test getExtensions behaviour if no arguments are given (None)"""
    from degrotesque import degrotesque
    p = tmp_path / "hello1.html"
    p.write_text("Hallo <b>Mama</b>")
    p = tmp_path / "hello2.html"
    p.write_text("Hallo <b>Mama</b>")
    files = degrotesque.getFiles(tmp_path, False, ["html"])
    checkFiles(["hello1.html", "hello2.html"], files, tmp_path)
    
def test_getFiles_multiple2(tmp_path):
    """Test getExtensions behaviour if no arguments are given (None)"""
    from degrotesque import degrotesque
    p = tmp_path / "hello1.html"
    p.write_text("Hallo <b>Mama</b>")
    p = tmp_path / "hello2.txt"
    p.write_text("Hallo <b>Mama</b>")
    files = degrotesque.getFiles(tmp_path, False, ["html"])
    checkFiles(["hello1.html"], files, tmp_path)
 
def test_getFiles_multiple_recursive1(tmp_path):
    """Test getExtensions behaviour if no arguments are given (None)"""
    from degrotesque import degrotesque
    p = tmp_path / "hello1.html"
    p.write_text("Hallo <b>Mama</b>")
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello2.html"
    p.write_text("Hallo <b>Mama</b>")
    files = degrotesque.getFiles(tmp_path, False, ["html"])
    checkFiles(["hello1.html"], files, tmp_path)
    
def test_getFiles_multiple_recursive2(tmp_path):
    """Test getExtensions behaviour if no arguments are given (None)"""
    from degrotesque import degrotesque
    p = tmp_path / "hello1.html"
    p.write_text("Hallo <b>Mama</b>")
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello2.html"
    p.write_text("Hallo <b>Mama</b>")
    files = degrotesque.getFiles(tmp_path, True, ["html"])
    checkFiles(["hello1.html", "sub/hello2.html"], files, tmp_path)
    

