#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
"""degrotesque - Tests for the helper.parse_to_skip method."""
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
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.split(__file__)[0], "..", "src"))
import helper


# --- test classes ------------------------------------------------------------
class TestDegrotesqueset_ToSkip(unittest.TestCase):
    """Testing the set_to_skip method"""

    def test_parse_to_skip_empty1(self):
        """Setting elements to skip to None - should be the defaults"""
        assert(helper.parse_to_skip(None)==helper.get_default_to_skip())

    def test_parse_to_skip_empty2(self):
        """Setting elements to skip to "" - should be the defaults"""
        assert(helper.parse_to_skip("")==helper.get_default_to_skip())

    def test_parse_to_skip_single(self):
        """Setting a single element to skip"""
        assert(helper.parse_to_skip("code")==["code"])

    def test_parse_to_skip_multiple(self):
        """Setting a single elements to skip"""
        assert(helper.parse_to_skip("code,test")==["code", "test"])

    def test_parse_to_skip_falseDivider(self):
        """Trying to set an unknown action
        : todo Check whether the user should be warned if something like this occurs"""
        assert(helper.parse_to_skip("code;test")==["code;test"])

