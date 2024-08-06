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
class TestDegrotesque_MarkDoxygen(unittest.TestCase):
    """Testing the _mark_markdown method"""

    def setUp(self):
        self._degrotesque = degrotesque.Degrotesque()
        self._marker = marker_begend.DegrotesqueBeginEndMarker([['/**', '*/'], ["///", "\n"]], ["java", "h", "cpp"])

    def test__mark_doxygen_textOnly1(self):
        """Text without markups only"""
        assert(self._marker.get_mask("Hallo")=="11111")

    def test__mark_doxygen_textOnly2(self):
        """Text without markups only"""
        assert(self._marker.get_mask("a")=="1")

    def test__mark_doxygen_textOnly3(self):
        """Text without markups only"""
        assert(self._marker.get_mask("Hallo Mama!")=="11111111111")



    def test__mark_doxygen_comment_singleline1(self):
        """A single comment in one line"""
        assert(self._marker.get_mask('Hallo\n/// Mama!\n')=="1111111110000001")

    def test__mark_doxygen_comment_singleline2(self):
        """A single comment in an own line"""
        assert(self._marker.get_mask('Hallo\n///Mama!\n')=="111111111000001")

    def test__mark_doxygen_comment_singleline3(self):
        """A multiple comments in multiple lines"""
        assert(self._marker.get_mask('Hallo\n/// Mama!\n/// I am a comment.\n')=="111111111000000111100000000000000001")

    def test__mark_doxygen_comment_singleline_double(self):
        """A multiple comments in multiple lines"""
        assert(self._marker.get_mask('Hallo\n/// Mama!/// I am a comment.\n')=="11111111100000000000000000000000001")

    def test__mark_doxygen_comment_singleline_noend(self):
        """A multiple comments in multiple lines"""
        assert(self._marker.get_mask('Hallo\n/// Mama!\n/// I am a comment.')=="11111111100000011110000000000000000")



    def test__mark_doxygen_comment_multiline1(self):
        """A single comment in one line"""
        assert(self._marker.get_mask('Hallo\n/**Mama!*/')=="1111111110000011")

    def test__mark_doxygen_comment_multiline2(self):
        """A single comment in an own line"""
        assert(self._marker.get_mask('Hallo\n/**\nMama!\n*/')=="111111111000000011")

    def test__mark_doxygen_comment_multiline3(self):
        """A single comment with multiple lines"""
        assert(self._marker.get_mask('Hallo\n/**\nMama!\nI am a comment.*/')=="111111111000000000000000000000011")

    def test__mark_doxygen_comment_multiline_double1(self):
        """A single comment with multiple lines"""
        assert(self._marker.get_mask('Hallo /**Mama!*/ I am a /**comment.*/')=="1111111110000011111111111110000000011")



    def test__mark_doxygen_link1(self):
        """A single comment with multiple lines"""
        assert(self._marker.get_mask('Hallo /** hallo http://www.krajzewicz.de hallo */')=="1111111110000000111111111111111111111111000000011")




    def test__mark_doxygen_broken(self):
        """Missing closing"""
        try:
            self._marker.get_mask('Hallo\n/**Mama!')
        except ValueError as e:
            assert type(e)==type(ValueError())
            assert str(e)=="Not a valid document"
            assert True
