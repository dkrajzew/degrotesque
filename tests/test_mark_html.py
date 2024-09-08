#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
"""degrotesque - Tests for the HTML/XML marker."""
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
import marker_html
import helper


# --- test classes ------------------------------------------------------------
class TestDegrotesque_MarkHTML(unittest.TestCase):
    """Testing the _mark_html method"""

    def setUp(self):
        self._marker = marker_html.DegrotesqueHTMLMarker()
        self._to_skip = helper.get_default_to_skip()

    def test__mark_html_textOnly1(self):
        """Text without markups only"""
        assert(self._marker.get_mask("Hallo", self._to_skip)=="00000")

    def test__mark_html_textOnly2(self):
        """Text without markups only"""
        assert(self._marker.get_mask("a", self._to_skip)=="0")


    def test__mark_html_simpleHTML1(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo <b>Mama!</b>", self._to_skip)=="000000111000001111")

    def test__mark_html_simpleHTML2(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("a<b></b>", self._to_skip)=="01111111")

    def test__mark_html_simpleHTML3(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("a<b>a</b>", self._to_skip)=="011101111")

    def test__mark_html_simpleHTML4(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("<b>a</b>", self._to_skip)=="11101111")

    def test__mark_html_simpleHTML5(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("<b>a</b>a", self._to_skip)=="111011110")


    def test__mark_html_php_plain1(self):
        """Parsing php"""
        assert(self._marker.get_mask("Hallo <?php a ?> ", self._to_skip)=="00000011111111110")

    def test__mark_html_php_plain2(self):
        """Parsing php"""
        assert(self._marker.get_mask("Hallo <? a ?> ", self._to_skip)=="00000011111110")

    def test__mark_html_php_unclosed(self):
        """Parsing php"""
        try:
            self._marker.get_mask("Hallo <? a", self._to_skip)
            assert False # pragma: no cover
        except ValueError as e:
            assert (type(e)==type(ValueError()))
            assert (str(e)=="Unclosed '<?' element at position 6.")


    def test__mark_html_asp_plain1(self):
        """Parsing asp"""
        assert(self._marker.get_mask("Hallo <% a %> ", self._to_skip)=="00000011111110")

    def test__mark_html_asp_unclosed(self):
        """Parsing asp"""
        try:
            self._marker.get_mask("Hallo <% a", self._to_skip)
            assert False # pragma: no cover
        except ValueError as e:
            assert (type(e)==type(ValueError()))
            assert (str(e)=="Unclosed '<%' element at position 6.")


    def test__mark_html_default1(self):
        """Parsing to skip"""
        assert(self._marker.get_mask("Hallo <code>a</code> ", self._to_skip)=="000000111111111111110")

    def test__mark_html_default_unclosed(self):
        """Parsing unclosed to skip"""
        try:
            self._marker.get_mask("Hallo <code>", self._to_skip)
            assert False # pragma: no cover
        except ValueError as e:
            assert (type(e)==type(ValueError()))
            assert (str(e)=="Unclosed '<code' element at position 6.")

    def test__mark_html_customToSkip(self):
        """Parsing custom to skip"""
        assert(self._marker.get_mask("Hallo <b>Mama!</b>", "b")=="000000111111111111")


    def test__mark_html_jsp1(self):
        """Parsing jsp/asp"""
        assert(self._marker.get_mask("Hallo <% a %> ", self._to_skip)=="00000011111110")


    def test__mark_html_comments_plain1(self):
        """Parsing comments"""
        assert(self._marker.get_mask("Hallo <!-- a --> ", self._to_skip)=="00000011111111110")

    def test__mark_html_comments_unclosed(self):
        """Parsing comments"""
        """Parsing php"""
        try:
            self._marker.get_mask("Hallo <!-- a", self._to_skip)
            assert False # pragma: no cover
        except ValueError as e:
            assert (type(e)==type(ValueError()))
            assert (str(e)=="Unclosed comment at position 6.")


    def test__mark_html_doctype1(self):
        """Parsing doctypes"""
        assert(self._marker.get_mask("Hallo <!DOCTYPE >a", self._to_skip)=="000000111111111110")

    def test__mark_html_doctype2(self):
        """Parsing doctypes"""
        assert(self._marker.get_mask("Hallo <!DOCTYPE <!ELEMENT >>a", self._to_skip)=="00000011111111111111111111110")


    def test__mark_html_toSkip_oddity1(self):
        """Oddity#1"""
        assert(self._marker.get_mask(" <(tm)>a</(tm)> ", "(tm)")=="0111111111111110")



    def test_masks_issn1(self):
        """Testing masks
        todo: Think about minusses and dealing with numbers"""
        assert(self._marker.get_mask(" ISSN 1001-1001 ")=="0111111111111110")
        assert(self._marker.get_mask(" ISBN 978-3-86680-192-9 ")=="000000111111111111111110")
        assert(self._marker.get_mask(" ISBN 979-3-86680-192-9 ")=="000000111111111111111110")
        assert(self._marker.get_mask(" ISBN 978-3-86680-192 ")=="0000001111111111111110")

    def test_masks_URL1(self):
        """Testing URL masking"""
        assert(self._marker.get_mask('Hallo http://www.krajzewicz.de hallo')=="000000111111111111111111111111000000")
        assert(self._marker.get_mask('http://www.krajzewicz.de hallo')=="111111111111111111111111000000")
        assert(self._marker.get_mask('Hallo http://www.krajzewicz.de')=="000000111111111111111111111111")
        assert(self._marker.get_mask('http://www.krajzewicz.de')=="111111111111111111111111")
