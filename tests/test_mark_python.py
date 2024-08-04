#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
"""degrotesque - Tests for the _mark_markdown method."""
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
sys.path.append(os.path.join(os.path.split(__file__)[0], "..", "degrotesque"))
import degrotesque
import marker_begend


# --- test classes ------------------------------------------------------------
class TestDegrotesque_MarkPython(unittest.TestCase):
    """Testing the _mark_markdown method"""

    def setUp(self):
        self._degrotesque = degrotesque.Degrotesque()
        self._marker = marker_begend.DegrotesqueBeginEndMarker('"""', '"""', ["py"])

    def test__mark_python_textOnly1(self):
        """Text without markups only"""
        assert(self._marker.get_mask("Hallo")=="11111")

    def test__mark_python_textOnly2(self):
        """Text without markups only"""
        assert(self._marker.get_mask("a")=="1")

    def test__mark_python_textOnly3(self):
        """Text without markups only"""
        assert(self._marker.get_mask("Hallo Mama!")=="11111111111")


    def test__mark_python_comment1(self):
        """A single comment in one line"""
        assert(self._marker.get_mask('Hallo\n"""Mama!"""')=="11111111100000111")

    def test__mark_python_comment2(self):
        """A single comment in an own line"""
        assert(self._marker.get_mask('Hallo\n"""\nMama!\n"""')=="1111111110000000111")

    def test__mark_python_comment3(self):
        """A single comment with multiple lines"""
        assert(self._marker.get_mask('Hallo\n"""\nMama!\nI am a comment."""')=="1111111110000000000000000000000111")


    def test__mark_python_broken(self):
        """Missing closing"""
        try:
            self._marker.get_mask('Hallo\n"""Mama!')
        except ValueError as e:
            assert type(e)==type(ValueError())
            assert str(e)=="Not a valid document"
            assert True
