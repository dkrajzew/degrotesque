from __future__ import print_function
# ===================================================================
# degrotesque - A web type setter.
#
# Tests for determining the file type
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
def test_filetype__two_html(capsys, tmp_path):
    """Whether two HTML files are processed"""
    import degrotesque
    p1 = tmp_path / "hello1.html"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.html"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    degrotesque.main(["-i", tmp_path])
    #captured = capsys.readouterr()
    #assert captured.out == ""
    #assert captured.err == ""
    assert p1.read_text() == "&#8220;Well &#8212; that&#39;s not what I had expected.&#8221;"
    assert p2.read_text() == "&#8220;Well &#8212; <code>that's</code> not what I had expected.&#8221;"


def test_filetype__two_text(capsys, tmp_path):
    """Whether two text files are processed
    
    The second file is recognized as HTML due to it's contents
    """
    import degrotesque
    p1 = tmp_path / "hello1.txt"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.txt"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    degrotesque.main(["-i", tmp_path])
    #captured = capsys.readouterr()
    #assert captured.out == ""
    #assert captured.err == ""
    assert p1.read_text() == "&#8220;Well &#8212; that&#39;s not what I had expected.&#8221;"
    assert p2.read_text() == "&#8220;Well &#8212; <code>that's</code> not what I had expected.&#8221;"


def test_filetype__two_text_explicit(capsys, tmp_path):
    """Whether two text files are processed
    
    The second file is recognized as HTML due to it's contents
    """
    import degrotesque
    p1 = tmp_path / "hello1.txt"
    p1.write_text("\"Well - that's not what I had expected.\"")
    p2 = tmp_path / "hello2.txt"
    p2.write_text("\"Well - <code>that's</code> not what I had expected.\"")
    degrotesque.main(["-i", tmp_path, "--text"])
    #captured = capsys.readouterr()
    #assert captured.out == ""
    #assert captured.err == ""
    assert p1.read_text() == "&#8220;Well &#8212; that&#39;s not what I had expected.&#8221;"
    assert p2.read_text() == "&#8220;Well &#8212; <code>that&#39;s</code> not what I had expected.&#8221;"
