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
import marker_text
import marker_md
import marker_html
import marker_begend
import marker_rst

# --- test functions ----------------------------------------------------------
def test_call_actions_unknown1(capsys):
    try: 
        degrotesque.prettify("\"Well - <code>that's</code> not what I had expected.\"", "sgml", replacement_format="unicode", actions=["foo"])
        assert False # pragma: no cover
    except ValueError as e:
        assert type(e)==type(ValueError())
        assert str(e)=="action 'foo' is not known"

def test_call_actions_unknown2(capsys):
    try: 
        degrotesque.prettify("\"Well - <code>that's</code> not what I had expected.\"", "sgml", replacement_format="unicode", actions="foo")
        assert False # pragma: no cover
    except ValueError as e:
        assert type(e)==type(ValueError())
        assert str(e)=="action 'foo' is not known"


def test_call_replacement_unknown1(capsys):
    try: 
        degrotesque.prettify("\"Well - that's not what I had expected.\"", "sgml", replacement_format="foo")
    except ValueError as e:
        assert type(e)==type(ValueError())
        assert str(e)=="Unknown target format 'foo'"


