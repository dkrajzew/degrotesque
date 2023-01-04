# ===================================================================
# degrotesque - A web type setter.
# Version 2.0.
#
# Tests for the mark method
#
# (c) Daniel Krajzewicz 2020-2023
# - daniel@krajzewicz.de
# - http://www.krajzewicz.de
# - https://github.com/dkrajzew/degrotesque
# - http://www.krajzewicz.de/blog/degrotesque.php
# 
# Available under the BSD license.
# ===================================================================


# --- imports -------------------------------------------------------
import unittest
import degrotesque


# --- classes -------------------------------------------------------
class TestDegrotesque_mark(unittest.TestCase):
    """Testing the _mark method"""

    def setUp(self):
        self._degrotesque = degrotesque.Degrotesque()

    def test__mark_textOnly1(self):
        """Text without markups only"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._mark("Hallo")=="00000")

    def test__mark_textOnly2(self):
        """Text without markups only"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._mark("a")=="0")


    def test__mark_simpleHTML1(self):
        """Some simple HTML markups"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._mark("Hallo <b>Mama!</b>")=="000000111000001111")

    def test__mark_simpleHTML2(self):
        """Some simple HTML markups"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._mark("a<b></b>")=="01111111")

    def test__mark_simpleHTML3(self):
        """Some simple HTML markups"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._mark("a<b>a</b>")=="011101111")

    def test__mark_simpleHTML4(self):
        """Some simple HTML markups"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._mark("<b>a</b>")=="11101111")

    def test__mark_simpleHTML5(self):
        """Some simple HTML markups"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._mark("<b>a</b>a")=="111011110")


    def test__mark_php_plain1(self):
        """Parsing php"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._mark("Hallo <?php a ?> ")=="00000011111111110")

    def test__mark_php_plain2(self):
        """Parsing php"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._mark("Hallo <? a ?> ")=="00000011111110")

    def test__mark_php_unclosed(self):
        """Parsing php"""
        self._degrotesque._restoreDefaultElementsToSkip()
        try: 
            self._degrotesque._mark("Hallo <? a")
            assert False
        except ValueError as e:
            assert (type(e)==type(ValueError()))
            assert (str(e)=="Unclosed '<?' element at position 8.")
        

    def test__mark_default1(self):
        """Parsing to skip"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._mark("Hallo <code>a</code> ")=="000000111111111111110")

    def test__mark_default_unclosed(self):
        """Parsing unclosed to skip"""
        self._degrotesque._restoreDefaultElementsToSkip()
        try:
            self._degrotesque._mark("Hallo <code>")
            assert False
        except ValueError as e:
            assert (type(e)==type(ValueError()))
            assert (str(e)=="Unclosed '<code' element at position 11.")

    def test__mark_customToSkip(self):
        """Parsing custom to skip"""
        self._degrotesque._restoreDefaultElementsToSkip()
        self._degrotesque.setToSkip("b")
        assert(self._degrotesque._mark("Hallo <b>Mama!</b>")=="000000111111111111")


    def test__mark_jsp1(self):
        """Parsing jsp/asp"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._mark("Hallo <% a %> ")=="00000011111110")


    def test__mark_comments1(self):
        """Parsing comments"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._mark("Hallo <!-- a --> ")=="00000011111111110")


    def test__mark_doctype1(self):
        """Parsing doctypes"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._mark("Hallo <!DOCTYPE >a")=="000000111111111110")

    def test__mark_doctype2(self):
        """Parsing doctypes"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._mark("Hallo <!DOCTYPE <!ELEMENT >>a")=="00000011111111111111111111110")


    def test__mark_toSkip_oddity1(self):
        """Oddity#1"""
        self._degrotesque._restoreDefaultElementsToSkip()
        self._degrotesque.setToSkip("(tm)")
        assert(self._degrotesque._mark(" <(tm)>a</(tm)> ")=="0111111111111110")

