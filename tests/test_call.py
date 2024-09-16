#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
"""degrotesque - Tests for direct call."""
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
import marker_text
import marker_md
import marker_html
import marker_begend
import marker_python
import marker_rst

# --- test functions ----------------------------------------------------------
def test_call_str_marker_html1(capsys):
    """For sgml (named)"""
    assert(degrotesque.prettify("\"Well - <code>that's</code> not what I had expected.\"", "sgml", replacement_format="unicode")=="&#8220;Well &#8212; <code>that's</code> not what I had expected.&#8221;")

def test_call_str_marker_text1(capsys):
    """For text (named)"""
    assert(degrotesque.prettify("\"Well - <code>that's</code> not what I had expected.\"", "text", replacement_format="unicode")=="&#8220;Well &#8212; <code>that&#39;s</code> not what I had expected.&#8221;")

def test_call_str_marker_md1(capsys):
    """For md (named)"""
    assert(degrotesque.prettify("\"Well - ```that's``` not what I had expected.\"", "md", replacement_format="unicode")=="&#8220;Well &#8212; ```that's``` not what I had expected.&#8221;")

def test_call_str_marker_rst1(capsys):
    """For rst (named)"""
    assert(degrotesque.prettify("\"Well - [that's]_ not what I had expected.\"", "rst", replacement_format="unicode")=="&#8220;Well &#8212; [that's]_ not what I had expected.&#8221;")

def test_call_str_marker_doxygen1(capsys):
    """For doxygen (named)"""
    assert(degrotesque.prettify("\"Well - /**that's*/ not what I had expected.\"", "doxygen", replacement_format="unicode")=="\"Well - /**that&#39;s*/ not what I had expected.\"")

def test_call_str_marker_python1(capsys):
    """For Python (named)"""
    assert(degrotesque.prettify("\"Well - \"\"\"that's\"\"\" not what I had expected.\"", "python", replacement_format="unicode")=="\"Well - \"\"\"that&#39;s\"\"\" not what I had expected.\"")



def test_call_obj_marker_html1(capsys):
    """For sgml (using a marker)"""
    marker = marker_html.DegrotesqueHTMLMarker()
    assert(degrotesque.prettify("\"Well - <code>that's</code> not what I had expected.\"", marker, replacement_format="unicode")=="&#8220;Well &#8212; <code>that's</code> not what I had expected.&#8221;")

def test_call_obj_marker_text1(capsys):
    """For text (using a marker)"""
    marker = marker_text.DegrotesqueTextMarker()
    assert(degrotesque.prettify("\"Well - <code>that's</code> not what I had expected.\"", marker, replacement_format="unicode")=="&#8220;Well &#8212; <code>that&#39;s</code> not what I had expected.&#8221;")

def test_call_obj_marker_md1(capsys):
    """For md (using a marker)"""
    marker = marker_md.DegrotesqueMDMarker()
    assert(degrotesque.prettify("\"Well - ```that's``` not what I had expected.\"", marker, replacement_format="unicode")=="&#8220;Well &#8212; ```that's``` not what I had expected.&#8221;")

def test_call_obj_marker_rst1(capsys):
    """For rst (using a marker)"""
    marker = marker_rst.DegrotesqueRSTMarker()
    assert(degrotesque.prettify("\"Well - [that's]_ not what I had expected.\"", marker, replacement_format="unicode")=="&#8220;Well &#8212; [that's]_ not what I had expected.&#8221;")

def test_call_obj_marker_doxygen1(capsys):
    """For doxygen (using a marker)"""
    marker = marker_begend.DegrotesqueDoxygenMarker()
    assert(degrotesque.prettify("\"Well - /**that's*/ not what I had expected.\"", marker, replacement_format="unicode")=="\"Well - /**that&#39;s*/ not what I had expected.\"")

def test_call_obj_marker_python1(capsys):
    """For Python (using a marker)"""
    marker = marker_python.DegrotesquePythonMarker()
    assert(degrotesque.prettify("\"Well - \"\"\"that's\"\"\" not what I had expected.\"", marker, replacement_format="unicode")=="\"Well - \"\"\"that&#39;s\"\"\" not what I had expected.\"")



def test_call_actions1(capsys):
    """No actions"""
    assert(degrotesque.prettify("\"Well - <code>that's</code> not what I had expected.\"", "sgml", replacement_format="unicode")=="&#8220;Well &#8212; <code>that's</code> not what I had expected.&#8221;")

def test_call_actions2(capsys):
    """One action"""
    assert(degrotesque.prettify("\"Well - <code>that's</code> not what I had expected.\"", "sgml", replacement_format="unicode", actions="quotes.english")=="&#8220;Well - <code>that's</code> not what I had expected.&#8221;")

def test_call_actions3(capsys):
    """Two actions as string"""
    assert(degrotesque.prettify("\"Well - <code>that's</code> not what I had expected.\"", "sgml", replacement_format="unicode", actions=["quotes.english,apostrophe"])=="&#8220;Well - <code>that's</code> not what I had expected.&#8221;")

def test_call_actions4(capsys):
    """Two actions as list"""
    assert(degrotesque.prettify("\"Well - <code>that's</code> not what I had expected.\"", "sgml", replacement_format="unicode", actions=["quotes.english", "apostrophe"])=="&#8220;Well - <code>that's</code> not what I had expected.&#8221;")

def test_call_actions5(capsys):
    """Actions are default (None)"""
    assert(degrotesque.prettify("\"Well - <code>that's</code> not what I had expected.\"", "sgml", replacement_format="unicode", actions=None)=="&#8220;Well &#8212; <code>that's</code> not what I had expected.&#8221;")



def test_call_to_skip1(capsys):
    """Skips default (None)"""
    assert(degrotesque.prettify("\"Well<pre> - </pre><code>that's</code> not what I had expected.\"", "sgml", replacement_format="unicode", to_skip=None)=="&#8220;Well<pre> - </pre><code>that's</code> not what I had expected.&#8221;")

def test_call_to_skip2(capsys):
    """Skips default"""
    assert(degrotesque.prettify("\"Well<pre> - </pre><code>that's</code> not what I had expected.\"", "sgml", replacement_format="unicode")=="&#8220;Well<pre> - </pre><code>that's</code> not what I had expected.&#8221;")

def test_call_to_skip3(capsys):
    """Skip pre as string"""
    assert(degrotesque.prettify("\"Well<pre> - </pre><code>that's</code> not what I had expected.\"", "sgml", replacement_format="unicode", to_skip="pre")=="&#8220;Well<pre> - </pre><code>that&#39;s</code> not what I had expected.&#8221;")

def test_call_to_skip4(capsys):
    """Skip pre as list"""
    assert(degrotesque.prettify("\"Well<pre> - </pre><code>that's</code> not what I had expected.\"", "sgml", replacement_format="unicode", to_skip=["pre"])=="&#8220;Well<pre> - </pre><code>that&#39;s</code> not what I had expected.&#8221;")

def test_call_to_skip5(capsys):
    """Skip code as string"""
    assert(degrotesque.prettify("\"Well<pre> - </pre><code>that's</code> not what I had expected.\"", "sgml", replacement_format="unicode", to_skip="code")=="&#8220;Well<pre> &#8212; </pre><code>that's</code> not what I had expected.&#8221;")

def test_call_to_skip6(capsys):
    """Skip code & pre as string"""
    assert(degrotesque.prettify("\"Well<pre> - </pre><code>that's</code> not what I had expected.\"", "sgml", replacement_format="unicode", to_skip="code,pre")=="&#8220;Well<pre> - </pre><code>that's</code> not what I had expected.&#8221;")

def test_call_to_skip7(capsys):
    """Skip code & pre as list"""
    assert(degrotesque.prettify("\"Well<pre> - </pre><code>that's</code> not what I had expected.\"", "sgml", replacement_format="unicode", to_skip=["code", "pre"])=="&#8220;Well<pre> - </pre><code>that's</code> not what I had expected.&#8221;")




def test_call_replacement_unicode1(capsys):
    """Replace by unicode"""
    assert(degrotesque.prettify("\"Well - that's not what I had expected.\"", "sgml", replacement_format="unicode")=="&#8220;Well &#8212; that&#39;s not what I had expected.&#8221;")

def test_call_replacement_html1(capsys):
    """Replace by HTML"""
    assert(degrotesque.prettify("\"Well - that's not what I had expected.\"", "sgml", replacement_format="html")=="&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;")

def test_call_replacement_text1(capsys):
    """Replace by text"""
    assert(degrotesque.prettify("\"Well - that's not what I had expected.\"", "sgml", replacement_format="char")=="“Well — that's not what I had expected.”")


