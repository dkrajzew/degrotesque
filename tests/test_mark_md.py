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
sys.path.append(os.path.join(os.path.split(__file__)[0], "..", "src"))
import degrotesque
import marker_md


# --- test classes ------------------------------------------------------------
class TestDegrotesque_MarkMarkdown(unittest.TestCase):
    """Testing the _mark_markdown method"""

    def setUp(self):
        self._marker = marker_md.DegrotesqueMDMarker()

    def test__mark_markdown_textOnly1(self):
        """Text without markups only"""
        assert(self._marker.get_mask("Hallo")=="00000")

    def test__mark_markdown_textOnly2(self):
        """Text without markups only"""
        assert(self._marker.get_mask("a")=="0")

    def test__mark_markdown_textOnly3(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo Mama!")=="00000000000")


    def test__mark_markdown_indent1a(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo\n\tMama!")=="000000111111")

    def test__mark_markdown_indent1b(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo\n    Mama!")=="000000111111111")

    def test__mark_markdown_indent2a(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo\n\tMama!\n\tIch bin ein\nCode")=="000000111111111111111111110000")

    def test__mark_markdown_indent2b(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo\n\tMama!\n    Ich bin ein\nCode")=="000000111111111111111111111110000")


    def test__mark_markdown_backtick1(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo `Mama`!")=="0000001111110")

    def test__mark_markdown_backtick2(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo ``Mama``!")=="000000111111110")

    def test__mark_markdown_backtick3(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo ```Mama```!")=="00000011111111110")

    def test__mark_markdown_nested_backtick1(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo `` `Mama` ``!")=="0000001111111111110")


    def test__mark_markdown_backtick1b(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo `Mama`")=="000000111111")

    def test__mark_markdown_backtick2b(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo ``Mama``")=="00000011111111")

    def test__mark_markdown_backtick3b(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo ```Mama```")=="0000001111111111")

    def test__mark_markdown_nested_backtick1b(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo `` `Mama` ``")=="000000111111111111")


    def test__mark_markdown_backtick4a(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo `Mama``Code`")=="000000111111111111")

    def test__mark_markdown_backtick4b(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo ``Mama```Code`")=="00000011111111111111")

    def test__mark_markdown_backtick4c(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo `Mama```Code``")=="00000011111111111111")
