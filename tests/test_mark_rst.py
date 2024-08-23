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
import marker_rst


# --- test classes ------------------------------------------------------------
class TestDegrotesque_MarkMarkdown(unittest.TestCase):
    """Testing the _mark_markdown method"""

    def setUp(self):
        self._marker = marker_rst.DegrotesqueRSTMarker()

    def test__mark_markdown_textOnly1(self):
        """Text without markups only"""
        assert(self._marker.get_mask("Hallo")=="00000")

    def test__mark_markdown_textOnly2(self):
        """Text without markups only"""
        assert(self._marker.get_mask("a")=="0")

    def test__mark_markdown_textOnly3(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo Mama!")=="00000000000")


    def test__mark_markdown_inline_literal1(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo\n``Mama!``")=="000000111111111")

    def test__mark_markdown_inline_literal2(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo ``Mama!``")=="000000111111111")


    def test__mark_markdown_inline_literal1(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo\n``Mama!``")=="000000111111111")

    def test__mark_markdown_inline_literal2(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo ``Mama!``")=="000000111111111")


    def test__mark_markdown_interpreted_text1(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo\n`Mama!`")=="0000001111111")

    def test__mark_markdown_interpreted_text2(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo `Mama!`")=="0000001111111")


    def test__mark_markdown_phrase_reference1(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo\n`Mama!`_")=="00000011111111")

    def test__mark_markdown_phrase_reference2(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo `Mama!`_")=="00000011111111")


    def test__mark_markdown_inline_internal_target1(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo\n_`Mama!`")=="00000011111111")

    def test__mark_markdown_inline_internal_target2(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo _`Mama!`")=="00000011111111")


    def test__mark_markdown_substitution_referece1(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo\n|Mama!|")=="0000001111111")

    def test__mark_markdown_substitution_referece2(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo |Mama!|")=="0000001111111")


    def test__mark_markdown_substitution_referece1(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo\n[Mama!]_")=="00000011111111")

    def test__mark_markdown_substitution_referece2(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo [Mama!]_")=="00000011111111")


