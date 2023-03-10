from __future__ import print_function
# ===================================================================
# degrotesque - A web type setter.
#
# Tests for the error handling in the main method
#
# (c) Daniel Krajzewicz 2020-2023
# daniel@krajzewicz.de
# - https://github.com/dkrajzew/degrotesque
# - http://www.krajzewicz.de/docs/degrotesque/index.html
# - http://www.krajzewicz.de
#
# Available under the BSD license.
# ===================================================================


# --- test functions ------------------------------------------------
def test_main__unknown_option_bool(capsys, tmp_path):
    """An unknown option is given as a bool"""
    import degrotesque
    p1 = tmp_path / "hello1.html"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.html"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    try:
        degrotesque.main(["-i", tmp_path, "-u"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err.replace("__main__.py", "degrotesque.py").replace("pytest", "degrotesque.py") == """Usage: 
  degrotesque.py [options]

degrotesque.py: error: no such option: -u
"""
    assert p1.read_text() == "\"Well - that's not what I had expected.\""
    assert p2.read_text() == "\"Well - <code>that's</code> not what I had expected.\""


def test_main__unknown_option_int(capsys, tmp_path):
    """An unknown option is given as an int"""
    import degrotesque
    p1 = tmp_path / "hello1.html"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.html"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    try:
        degrotesque.main(["-i", tmp_path, "--foo", "bar"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err.replace("__main__.py", "degrotesque.py").replace("pytest", "degrotesque.py") == """Usage: 
  degrotesque.py [options]

degrotesque.py: error: no such option: --foo
"""
    assert p1.read_text() == "\"Well - that's not what I had expected.\""
    assert p2.read_text() == "\"Well - <code>that's</code> not what I had expected.\""


def test_main__format__unknown(capsys, tmp_path):
    """An unknown option is given as bool"""
    import degrotesque
    p1 = tmp_path / "hello1.html"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.html"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    try:
        degrotesque.main(["-i", tmp_path, "--format", "foo"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==3
    captured = capsys.readouterr()
    assert captured.err == ""
    assert captured.out.replace("__main__.py", "degrotesque.py").replace("pytest", "degrotesque.py") == """Unknown target format 'foo'
"""
    assert p1.read_text() == "\"Well - that's not what I had expected.\""
    assert p2.read_text() == "\"Well - <code>that's</code> not what I had expected.\""


def test_main__document_broken1(capsys, tmp_path):
    """An unknown option is given as bool"""
    import degrotesque
    p1 = tmp_path / "hello1.html"
    p1.write_text("<p \"Well - that's not what I had expected.\"")
    try:
        degrotesque.main(["-i", tmp_path])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==4
    captured = capsys.readouterr()
    assert captured.err == ""
    assert captured.out.replace(str(tmp_path), "<DIR>").replace("\\", "/").replace("__main__.py", "degrotesque.py").replace("pytest", "degrotesque.py") == """Processing <DIR>/hello1.html
Unclosed element at 1
"""
    assert p1.read_text() == "<p \"Well - that's not what I had expected.\""


def test_main__document_broken2(capsys, tmp_path):
    """An unknown option is given as bool"""
    import degrotesque
    p1 = tmp_path / "hello1.html"
    p1.write_text("<pre> <pre \"Well - that's not what I had expected.\"")
    try:
        degrotesque.main(["-i", tmp_path])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==4
    captured = capsys.readouterr()
    assert captured.err == ""
    assert captured.out.replace(str(tmp_path), "<DIR>").replace("\\", "/").replace("__main__.py", "degrotesque.py").replace("pytest", "degrotesque.py") == """Processing <DIR>/hello1.html
Unclosed '<pre' element at position 4.
"""
    assert p1.read_text() == "<pre> <pre \"Well - that's not what I had expected.\""

