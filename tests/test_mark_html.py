# ===================================================================
# degrotesque - A web type setter.
#
# Tests for the _markHTML method
#
# (c) Daniel Krajzewicz 2020-2023
# daniel@krajzewicz.de
# - https://github.com/dkrajzew/degrotesque
# - http://www.krajzewicz.de/docs/degrotesque/index.html
# - http://www.krajzewicz.de
#
# Available under the BSD license.
# ===================================================================


# --- imports -------------------------------------------------------
import unittest
import degrotesque


# --- classes -------------------------------------------------------
class TestDegrotesque_markHTML(unittest.TestCase):
    """Testing the _markHTML method"""

    def setUp(self):
        self._degrotesque = degrotesque.Degrotesque()

    def test__markHTML_textOnly1(self):
        """Text without markups only"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._markHTML("Hallo")=="00000")

    def test__markHTML_textOnly2(self):
        """Text without markups only"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._markHTML("a")=="0")


    def test__markHTML_simpleHTML1(self):
        """Some simple HTML markups"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._markHTML("Hallo <b>Mama!</b>")=="000000111000001111")

    def test__markHTML_simpleHTML2(self):
        """Some simple HTML markups"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._markHTML("a<b></b>")=="01111111")

    def test__markHTML_simpleHTML3(self):
        """Some simple HTML markups"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._markHTML("a<b>a</b>")=="011101111")

    def test__markHTML_simpleHTML4(self):
        """Some simple HTML markups"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._markHTML("<b>a</b>")=="11101111")

    def test__markHTML_simpleHTML5(self):
        """Some simple HTML markups"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._markHTML("<b>a</b>a")=="111011110")


    def test__markHTML_php_plain1(self):
        """Parsing php"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._markHTML("Hallo <?php a ?> ")=="00000011111111110")

    def test__markHTML_php_plain2(self):
        """Parsing php"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._markHTML("Hallo <? a ?> ")=="00000011111110")

    def test__markHTML_php_unclosed(self):
        """Parsing php"""
        self._degrotesque._restoreDefaultElementsToSkip()
        try:
            self._degrotesque._markHTML("Hallo <? a")
            assert False # pragma: no cover
        except ValueError as e:
            assert (type(e)==type(ValueError()))
            assert (str(e)=="Unclosed '<?' element at position 8.")


    def test__markHTML_default1(self):
        """Parsing to skip"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._markHTML("Hallo <code>a</code> ")=="000000111111111111110")

    def test__markHTML_default_unclosed(self):
        """Parsing unclosed to skip"""
        self._degrotesque._restoreDefaultElementsToSkip()
        try:
            self._degrotesque._markHTML("Hallo <code>")
            assert False # pragma: no cover
        except ValueError as e:
            assert (type(e)==type(ValueError()))
            assert (str(e)=="Unclosed '<code' element at position 11.")

    def test__markHTML_customToSkip(self):
        """Parsing custom to skip"""
        self._degrotesque._restoreDefaultElementsToSkip()
        self._degrotesque.setToSkip("b")
        assert(self._degrotesque._markHTML("Hallo <b>Mama!</b>")=="000000111111111111")


    def test__markHTML_jsp1(self):
        """Parsing jsp/asp"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._markHTML("Hallo <% a %> ")=="00000011111110")


    def test__markHTML_comments1(self):
        """Parsing comments"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._markHTML("Hallo <!-- a --> ")=="00000011111111110")


    def test__markHTML_doctype1(self):
        """Parsing doctypes"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._markHTML("Hallo <!DOCTYPE >a")=="000000111111111110")

    def test__markHTML_doctype2(self):
        """Parsing doctypes"""
        self._degrotesque._restoreDefaultElementsToSkip()
        assert(self._degrotesque._markHTML("Hallo <!DOCTYPE <!ELEMENT >>a")=="00000011111111111111111111110")


    def test__markHTML_toSkip_oddity1(self):
        """Oddity#1"""
        self._degrotesque._restoreDefaultElementsToSkip()
        self._degrotesque.setToSkip("(tm)")
        assert(self._degrotesque._markHTML(" <(tm)>a</(tm)> ")=="0111111111111110")

