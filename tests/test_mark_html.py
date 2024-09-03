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

    def test__mark_html_textOnly1(self):
        """Text without markups only"""
        assert(self._marker.get_mask("Hallo")=="00000")

    def test__mark_html_textOnly2(self):
        """Text without markups only"""
        assert(self._marker.get_mask("a")=="0")


    def test__mark_html_simpleHTML1(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("Hallo <b>Mama!</b>")=="000000111000001111")

    def test__mark_html_simpleHTML2(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("a<b></b>")=="01111111")

    def test__mark_html_simpleHTML3(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("a<b>a</b>")=="011101111")

    def test__mark_html_simpleHTML4(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("<b>a</b>")=="11101111")

    def test__mark_html_simpleHTML5(self):
        """Some simple HTML markups"""
        assert(self._marker.get_mask("<b>a</b>a")=="111011110")


    def test__mark_html_php_plain1(self):
        """Parsing php"""
        assert(self._marker.get_mask("Hallo <?php a ?> ")=="00000011111111110")

    def test__mark_html_php_plain2(self):
        """Parsing php"""
        assert(self._marker.get_mask("Hallo <? a ?> ")=="00000011111110")

    def test__mark_html_php_unclosed(self):
        """Parsing php"""
        try:
            self._marker.get_mask("Hallo <? a")
            assert False # pragma: no cover
        except ValueError as e:
            assert (type(e)==type(ValueError()))
            assert (str(e)=="Unclosed '<?' element at position 6.")


    def test__mark_html_asp_plain1(self):
        """Parsing php"""
        assert(self._marker.get_mask("Hallo <% a %> ")=="00000011111110")

    def test__mark_html_asp_unclosed(self):
        """Parsing php"""
        try:
            self._marker.get_mask("Hallo <% a")
            assert False # pragma: no cover
        except ValueError as e:
            assert (type(e)==type(ValueError()))
            assert (str(e)=="Unclosed '<%' element at position 6.")


    def test__mark_html_default1(self):
        """Parsing to skip"""
        assert(self._marker.get_mask("Hallo <code>a</code> ")=="000000111111111111110")

    def test__mark_html_default_unclosed(self):
        """Parsing unclosed to skip"""
        try:
            self._marker.get_mask("Hallo <code>")
            assert False # pragma: no cover
        except ValueError as e:
            assert (type(e)==type(ValueError()))
            assert (str(e)=="Unclosed '<code' element at position 6.")

    def test__mark_html_customToSkip(self):
        """Parsing custom to skip"""
        assert(self._marker.get_mask("Hallo <b>Mama!</b>", "b")=="000000111111111111")


    def test__mark_html_jsp1(self):
        """Parsing jsp/asp"""
        assert(self._marker.get_mask("Hallo <% a %> ")=="00000011111110")


    def test__mark_html_comments_plain1(self):
        """Parsing comments"""
        assert(self._marker.get_mask("Hallo <!-- a --> ")=="00000011111111110")

    def test__mark_html_comments_unclosed(self):
        """Parsing comments"""
        """Parsing php"""
        try:
            self._marker.get_mask("Hallo <!-- a")
            assert False # pragma: no cover
        except ValueError as e:
            assert (type(e)==type(ValueError()))
            assert (str(e)=="Unclosed comment at position 6.")


    def test__mark_html_doctype1(self):
        """Parsing doctypes"""
        assert(self._marker.get_mask("Hallo <!DOCTYPE >a")=="000000111111111110")

    def test__mark_html_doctype2(self):
        """Parsing doctypes"""
        assert(self._marker.get_mask("Hallo <!DOCTYPE <!ELEMENT >>a")=="00000011111111111111111111110")


    def test__mark_html_toSkip_oddity1(self):
        """Oddity#1"""
        assert(self._marker.get_mask(" <(tm)>a</(tm)> ", "(tm)")=="0111111111111110")

