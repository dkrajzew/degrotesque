#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
"""degrotesque - Tests for the Python marker."""
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
import marker_python


# --- test classes ------------------------------------------------------------
class TestDegrotesque_MarkPython(unittest.TestCase):
    """Testing the _mark_markdown method"""

    def setUp(self):
        self._marker = marker_python.DegrotesquePythonMarker()

    def test__mark_python_textOnly1(self):
        """Text without markups only"""
        assert(self._marker.get_mask("Hallo")=="11111")

    def test__mark_python_textOnly2(self):
        """Text without markups only"""
        assert(self._marker.get_mask("a")=="1")

    def test__mark_python_textOnly3(self):
        """Text without markups only"""
        assert(self._marker.get_mask("Hallo Mama!")=="11111111111")



    def test__mark_python_comment_singleline1(self):
        """A single comment in one line"""
        assert(self._marker.get_mask('Hallo\n# Mama!\n')=="11111110000001")

    def test__mark_python_comment_singleline2(self):
        """A single comment in an own line"""
        assert(self._marker.get_mask('Hallo\n#Mama!\n')=="1111111000001")

    def test__mark_python_comment_singleline3(self):
        """A multiple comments in multiple lines"""
        assert(self._marker.get_mask('Hallo\n# Mama!\n# I am a comment.\n')=="11111110000001100000000000000001")

    def test__mark_python_comment_singleline_double(self):
        """A multiple comments in multiple lines"""
        assert(self._marker.get_mask('Hallo\n# Mama!# I am a comment.\n')=="1111111000000000000000000000001")

    def test__mark_python_comment_singleline_noend(self):
        """A multiple comments in multiple lines"""
        assert(self._marker.get_mask('Hallo\n# Mama!\n# I am a comment.')=="1111111000000110000000000000000")



    def test__mark_python_comment_multiline1(self):
        """A single comment in one line"""
        assert(self._marker.get_mask('Hallo\n"""Mama!"""')=="11111111100000111")

    def test__mark_python_comment_multiline2(self):
        """A single comment in an own line"""
        assert(self._marker.get_mask('Hallo\n"""\nMama!\n"""')=="1111111110000000111")

    def test__mark_python_comment_multiline3(self):
        """A single comment with multiple lines"""
        assert(self._marker.get_mask('Hallo\n"""\nMama!\nI am a comment."""')=="1111111110000000000000000000000111")

    def test__mark_python_comment_multiline_double1(self):
        """A single comment with multiple lines"""
        assert(self._marker.get_mask('Hallo """Mama!""" I am a """comment."""')=="111111111000001111111111111100000000111")



    def test__mark_python_pydoctest1(self):
        """pydoc"""
        assert(self._marker.get_mask("Hallo\n>>> Hello Mama!")=="111111111111111111111")

    def test__mark_python_pydoctest2(self):
        """pydoc"""
        assert(self._marker.get_mask("Hallo\n>>> Hello Mama!\n\nHallo")=="1111111111111111111111111111")

    def test__mark_python_pydoctest3(self):
        """pydoc"""
        assert(self._marker.get_mask("Hallo\n>>> Hello Mama!\nHallo\n\nHallo")=="1111111111111111111111111111111111")

    def test__mark_python_pydoctest4(self):
        """pydoc"""
        assert(self._marker.get_mask("Hallo\n>>> Hello Mama!\nHallo\n\nHallo\n>>> Hello Mama!\n\n")=="1111111111111111111111111111111111111111111111111111")

    def test__mark_python_pydoctest5(self):
        """pydoc"""
        assert(self._marker.get_mask(">>> Hello Mama!")=="111111111111111")
        
    def test__mark_markdown_pydoctest6(self):
        """pydoc"""
        assert(self._marker.get_mask("\"\"\"Hallo\n>>> Hello Mama!\"\"\"")=="111000000111111111111111111")

    def test__mark_markdown_pydoctest7(self):
        """pydoc"""
        assert(self._marker.get_mask("\"\"\"Hallo\n>>> Hello Mama!\n\nHallo\"\"\"")=="1110000001111111111111111000000111")

    def test__mark_markdown_pydoctest8(self):
        """pydoc"""
        assert(self._marker.get_mask("\"\"\"Hallo\n>>> Hello Mama!\nHallo\n\nHallo\"\"\"")=="1110000001111111111111111111111000000111")

    def test__mark_markdown_pydoctest9(self):
        """pydoc"""
        assert(self._marker.get_mask("\"\"\"Hallo\n>>> Hello Mama!\nHallo\n\nHallo\n>>> Hello Mama!\n\n\"\"\"")=="1110000001111111111111111111111000000011111111111111110111")

    def test__mark_markdown_pydoctest10(self):
        """pydoc"""
        assert(self._marker.get_mask("\"\"\">>> Hello Mama!\"\"\"")=="111111111111111111111")



        

    def test__mark_python_link1(self):
        """Masking links in comments"""
        assert(self._marker.get_mask('Hallo """ hallo http://www.krajzewicz.de hallo """')=="11111111100000001111111111111111111111110000000111")



    def test__mark_python_broken(self):
        """Missing closing"""
        assert(self._marker.get_mask('Hallo\n"""Mama!')=="11111111111111")



    def test_masks_issn1(self):
        """Testing masks
        todo: Think about minusses and dealing with numbers"""
        assert(self._marker.get_mask(" ISSN 1001-1001 ")=="1111111111111111")
        assert(self._marker.get_mask(" ISBN 978-3-86680-192-9 ")=="111111111111111111111111")
        assert(self._marker.get_mask(" ISBN 979-3-86680-192-9 ")=="111111111111111111111111")
        assert(self._marker.get_mask(" ISBN 978-3-86680-192 ")=="1111111111111111111111")

    def test_masks_issn2(self):
        """Testing masks
        todo: Think about minusses and dealing with numbers"""
        assert(self._marker.get_mask("# ISSN 1001-1001 ")=="10111111111111110")
        assert(self._marker.get_mask("# ISBN 978-3-86680-192-9 ")=="1000000111111111111111110")
        assert(self._marker.get_mask("# ISBN 979-3-86680-192-9 ")=="1000000111111111111111110")
        assert(self._marker.get_mask("# ISBN 978-3-86680-192 ")=="10000001111111111111110")

    def test_masks_URL1(self):
        """Testing URL masking"""
        assert(self._marker.get_mask('Hallo http://www.krajzewicz.de hallo')=="111111111111111111111111111111111111")
        assert(self._marker.get_mask('http://www.krajzewicz.de hallo')=="111111111111111111111111111111")
        assert(self._marker.get_mask('Hallo http://www.krajzewicz.de')=="111111111111111111111111111111")
        assert(self._marker.get_mask('http://www.krajzewicz.de')=="111111111111111111111111")

    def test_masks_URL2(self):
        """Testing URL masking"""
        assert(self._marker.get_mask('# Hallo http://www.krajzewicz.de hallo')=="10000000111111111111111111111111000000")
        assert(self._marker.get_mask('# http://www.krajzewicz.de hallo')=="10111111111111111111111111000000")
        assert(self._marker.get_mask('# Hallo http://www.krajzewicz.de')=="10000000111111111111111111111111")
        assert(self._marker.get_mask('# http://www.krajzewicz.de')=="10111111111111111111111111")
