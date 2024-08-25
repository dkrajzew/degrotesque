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


    def test__mark_markdown_substitution_reference1(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo\n|Mama!|")=="0000001111111")

    def test__mark_markdown_substitution_reference2(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo |Mama!|")=="0000001111111")


    def test__mark_markdown_reference1(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo\n[Mama!]_")=="00000011111111")

    def test__mark_markdown_reference2(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo [Mama!]_")=="00000011111111")


    def test__mark_markdown_literal_block1(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo\n::\n\nHello Mama!")=="000000111000000000000")

    def test__mark_markdown_literal_block2(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo\n::\n\tHello Mama!")=="000000111111111111111")

    def test__mark_markdown_literal_block3(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo\n::\n\tHello Mama!\n\ntest")=="000000111111111111111100000")

    def test__mark_markdown_literal_block4(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo\n::\n\tHello Mama!\n\ntest::\n\tHello Mama!")=="000000111111111111111100000111111111111111")

    def test__mark_markdown_literal_block5(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("::\n\tHello Mama!")=="111111111111111")


    def test__mark_markdown_pydoctest1(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo\n>>> Hello Mama!")=="000000111111111111111")

    def test__mark_markdown_pydoctest2(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo\n>>> Hello Mama!\n\nHallo")=="0000001111111111111111000000")

    def test__mark_markdown_pydoctest3(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo\n>>> Hello Mama!\nHallo\n\nHallo")=="0000001111111111111111111111000000")

    def test__mark_markdown_pydoctest4(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo\n>>> Hello Mama!\nHallo\n\nHallo\n>>> Hello Mama!\n\n")=="0000001111111111111111111111000000011111111111111110")

    def test__mark_markdown_pydoctest5(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask(">>> Hello Mama!")=="111111111111111")



    def test__mixed1(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo ``Mama!`` `Mama!` ``Mama!``")=="000000111111111011111110111111111")
