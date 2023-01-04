from __future__ import print_function
# ===================================================================
# degrotesque - A web type setter.
# Version 2.0.
#
# Tests for the main method
#
# (c) Daniel Krajzewicz 2020-2023
# - daniel@krajzewicz.de
# - http://www.krajzewicz.de
# - https://github.com/dkrajzew/degrotesque
# - http://www.krajzewicz.de/blog/degrotesque.php
# 
# Available under the BSD license.
# ===================================================================


# --- test functions ------------------------------------------------
def test_main_empty(capsys):
    """Test behaviour if no arguments are given"""
    import degrotesque
    try:
        degrotesque.main([])
        assert False
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert captured.err.replace("__main__.py", "degrotesque.py") == "Error: no input file(s) given...\nUsage: degrotesque.py -i <FILE>[,<FILE>]* [options]+\n"
    assert captured.out == ""
    

def test_main_help(capsys):
    """Test behaviour when help is wished"""
    import degrotesque
    try:
        degrotesque.main(["--help"])
        assert False
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert captured.out.replace("__main__.py", "degrotesque.py") == """Usage: usage:
  degrotesque.py [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -i INPUT, --input=INPUT
                        Defines files/folder to process
  -r, --recursive       Whether a given path shall be processed recursively
  -B, --no-backup       Whether no backup shall be generated
  -u, --unicode         Use unicode characters instead of HTML entities
  -e EXTENSIONS, --extensions=EXTENSIONS
                        Defines the extensions of files to process
  -E ENCODING, --encoding=ENCODING
                        File encoding (default: 'utf-8')
  -s SKIP, --skip=SKIP  Defines the elements which contents shall not be
                        changed
  -a ACTIONS, --actions=ACTIONS
                        Defines the actions to perform
"""
    assert captured.err == ""
    

def test_main_run1(capsys, tmp_path):
    """Test behaviour on plain usage"""
    import degrotesque
    p1 = tmp_path / "hello1.html"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.html"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    degrotesque.main(["-i", tmp_path])
    assert p1.read_text() == "&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;"
    assert p2.read_text() == "&ldquo;Well &mdash; <code>that's</code> not what I had expected.&rdquo;"


def test_main_run2(capsys, tmp_path):
    """Test behaviour on plain usage"""
    import degrotesque
    p1 = tmp_path / "hello1.html"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.html"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    degrotesque.main(["-i", tmp_path, "-u"])
    assert p1.read_text() == "&#8220;Well &#8212; that&#39;s not what I had expected.&#8221;"
    assert p2.read_text() == "&#8220;Well &#8212; <code>that's</code> not what I had expected.&#8221;"
    