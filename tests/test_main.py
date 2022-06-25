from __future__ import print_function
"""degrotesque.py

A tiny web type setter.

Tests for degrotesque's main method.

(c) Daniel Krajzewicz 2020-2022
daniel@krajzewicz.de
http://www.krajzewicz.de
https://github.com/dkrajzew/degrotesque
http://www.krajzewicz.de/blog/degrotesque.php

Available under EPL 2.0 or later, all rights reserved
"""


# --- test functions ------------------------------------------------
def test_main_empty(capsys):
    """Test behaviour if no arguments are given"""
    from degrotesque import degrotesque
    try:
        degrotesque.main([])
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert captured.err.replace("__main__.py", "degrotesque.py") == "Error: no input file(s) given...\nUsage: degrotesque.py [options]+ -i <FILE>[,<FILE>]*\n"
    assert captured.out == ""
    

def test_main_help_long(capsys):
    """Test behaviour when help is wished"""
    from degrotesque import degrotesque
    try:
        degrotesque.main(["--help"])
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
  -E ENCODING, --encoding=ENCODING
                        File encoding (default: 'utf-8'
  -r, --recursive       Whether a given path shall be processed recursively
  -B, --no-backup       Whether no backup shall be generated
  -e EXTENSIONS, --extensions=EXTENSIONS
                        Defines the extensions of files to process
  -s SKIP, --skip=SKIP  Defines the elements which contents shall not be
                        changed
  -a ACTIONS, --actions=ACTIONS
                        Defines the actions to perform
"""
    assert captured.err == ""
    

    
    