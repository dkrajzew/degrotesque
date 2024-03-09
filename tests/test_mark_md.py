# ===================================================================
# degrotesque - A web type setter.
#
# Tests for the _mark_markdown method
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
class TestDegrotesque_MarkMarkdown(unittest.TestCase):
    """Testing the _mark_markdown method"""

    def setUp(self):
        self._degrotesque = degrotesque.Degrotesque()

    def test__mark_markdown_textOnly1(self):
        """Text without markups only"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._degrotesque._mark_markdown("Hallo")=="00000")

    def test__mark_markdown_textOnly2(self):
        """Text without markups only"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._degrotesque._mark_markdown("a")=="0")

    def test__mark_markdown_textOnly3(self):
        """Some simple HTML markups"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._degrotesque._mark_markdown("Hallo Mama!")=="00000000000")


    def test__mark_markdown_indent1a(self):
        """Some simple HTML markups"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._degrotesque._mark_markdown("Hallo\n\tMama!")=="000000111111")

    def test__mark_markdown_indent1b(self):
        """Some simple HTML markups"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._degrotesque._mark_markdown("Hallo\n    Mama!")=="000000111111111")

    def test__mark_markdown_indent2a(self):
        """Some simple HTML markups"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._degrotesque._mark_markdown("Hallo\n\tMama!\n\tIch bin ein\nCode")=="000000111111111111111111110000")

    def test__mark_markdown_indent2b(self):
        """Some simple HTML markups"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._degrotesque._mark_markdown("Hallo\n\tMama!\n    Ich bin ein\nCode")=="000000111111111111111111111110000")


    def test__mark_markdown_backtick1(self):
        """Some simple HTML markups"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._degrotesque._mark_markdown("Hallo `Mama`!")=="0000001111110")

    def test__mark_markdown_backtick2(self):
        """Some simple HTML markups"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._degrotesque._mark_markdown("Hallo ``Mama``!")=="000000111111110")

    def test__mark_markdown_backtick3(self):
        """Some simple HTML markups"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._degrotesque._mark_markdown("Hallo ```Mama```!")=="00000011111111110")

    def test__mark_markdown_nested_backtick1(self):
        """Some simple HTML markups"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._degrotesque._mark_markdown("Hallo `` `Mama` ``!")=="0000001111111111110")


    def test__mark_markdown_backtick1b(self):
        """Some simple HTML markups"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._degrotesque._mark_markdown("Hallo `Mama`")=="000000111111")

    def test__mark_markdown_backtick2b(self):
        """Some simple HTML markups"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._degrotesque._mark_markdown("Hallo ``Mama``")=="00000011111111")

    def test__mark_markdown_backtick3b(self):
        """Some simple HTML markups"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._degrotesque._mark_markdown("Hallo ```Mama```")=="0000001111111111")

    def test__mark_markdown_nested_backtick1b(self):
        """Some simple HTML markups"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._degrotesque._mark_markdown("Hallo `` `Mama` ``")=="000000111111111111")


    def test__mark_markdown_backtick4a(self):
        """Some simple HTML markups"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._degrotesque._mark_markdown("Hallo `Mama``Code`")=="000000111111111111")

    def test__mark_markdown_backtick4b(self):
        """Some simple HTML markups"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._degrotesque._mark_markdown("Hallo ``Mama```Code`")=="00000011111111111111")

    def test__mark_markdown_backtick4c(self):
        """Some simple HTML markups"""
        self._degrotesque._restore_default_elements_to_skip()
        assert(self._degrotesque._mark_markdown("Hallo `Mama```Code``")=="00000011111111111111")
