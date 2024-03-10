#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
"""degrotesque - Tests for the _mark_html method."""
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
from degrotesque import degrotesque
from degrotesque import html_marker


# --- test classes ------------------------------------------------------------
class TestDegrotesque_MarkHTML(unittest.TestCase):
    """Testing the _mark_html method"""

    def setUp(self):
        self._degrotesque = degrotesque.Degrotesque()
        self._marker = html_marker.DegrotesqueHTMLMarker()

    def test__mark_html_textOnly1(self):
        """Text without markups only"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._marker.get_mask("Hallo", self._degrotesque._elements_to_skip)=="00000")

    def test__mark_html_textOnly2(self):
        """Text without markups only"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._marker.get_mask("a", self._degrotesque._elements_to_skip)=="0")


    def test__mark_html_simpleHTML1(self):
        """Some simple HTML markups"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._marker.get_mask("Hallo <b>Mama!</b>", self._degrotesque._elements_to_skip)=="000000111000001111")

    def test__mark_html_simpleHTML2(self):
        """Some simple HTML markups"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._marker.get_mask("a<b></b>", self._degrotesque._elements_to_skip)=="01111111")

    def test__mark_html_simpleHTML3(self):
        """Some simple HTML markups"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._marker.get_mask("a<b>a</b>", self._degrotesque._elements_to_skip)=="011101111")

    def test__mark_html_simpleHTML4(self):
        """Some simple HTML markups"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._marker.get_mask("<b>a</b>", self._degrotesque._elements_to_skip)=="11101111")

    def test__mark_html_simpleHTML5(self):
        """Some simple HTML markups"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._marker.get_mask("<b>a</b>a", self._degrotesque._elements_to_skip)=="111011110")


    def test__mark_html_php_plain1(self):
        """Parsing php"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._marker.get_mask("Hallo <?php a ?> ", self._degrotesque._elements_to_skip)=="00000011111111110")

    def test__mark_html_php_plain2(self):
        """Parsing php"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._marker.get_mask("Hallo <? a ?> ", self._degrotesque._elements_to_skip)=="00000011111110")

    def test__mark_html_php_unclosed(self):
        """Parsing php"""
        self._degrotesque._restore_default_elements_to_skip()
        try:
            self._marker.get_mask("Hallo <? a", self._degrotesque._elements_to_skip)
            assert False # pragma: no cover
        except ValueError as e:
            assert (type(e)==type(ValueError()))
            assert (str(e)=="Unclosed '<?' element at position 8.")


    def test__mark_html_default1(self):
        """Parsing to skip"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._marker.get_mask("Hallo <code>a</code> ", self._degrotesque._elements_to_skip)=="000000111111111111110")

    def test__mark_html_default_unclosed(self):
        """Parsing unclosed to skip"""
        self._degrotesque._restore_default_elements_to_skip()
        try:
            self._marker.get_mask("Hallo <code>", self._degrotesque._elements_to_skip)
            assert False # pragma: no cover
        except ValueError as e:
            assert (type(e)==type(ValueError()))
            assert (str(e)=="Unclosed '<code' element at position 11.")

    def test__mark_html_customToSkip(self):
        """Parsing custom to skip"""
        self._degrotesque._restore_default_elements_to_skip()
        self._degrotesque.set_to_skip("b")
        assert(self._marker.get_mask("Hallo <b>Mama!</b>", self._degrotesque._elements_to_skip)=="000000111111111111")


    def test__mark_html_jsp1(self):
        """Parsing jsp/asp"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._marker.get_mask("Hallo <% a %> ", self._degrotesque._elements_to_skip)=="00000011111110")


    def test__mark_html_comments1(self):
        """Parsing comments"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._marker.get_mask("Hallo <!-- a --> ", self._degrotesque._elements_to_skip)=="00000011111111110")


    def test__mark_html_doctype1(self):
        """Parsing doctypes"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._marker.get_mask("Hallo <!DOCTYPE >a", self._degrotesque._elements_to_skip)=="000000111111111110")

    def test__mark_html_doctype2(self):
        """Parsing doctypes"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._marker.get_mask("Hallo <!DOCTYPE <!ELEMENT >>a", self._degrotesque._elements_to_skip)=="00000011111111111111111111110")


    def test__mark_html_toSkip_oddity1(self):
        """Oddity#1"""
        self._degrotesque._restore_default_elements_to_skip()
        self._degrotesque.set_to_skip("(tm)")
        assert(self._marker.get_mask(" <(tm)>a</(tm)> ", self._degrotesque._elements_to_skip)=="0111111111111110")

