# ===================================================================
# degrotesque - A web type setter.
#
# Tests for the set_to_skip method
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
class TestDegrotesqueset_ToSkip(unittest.TestCase):
    """Testing the set_to_skip method"""

    def setUp(self):
        self._degrotesque = degrotesque.Degrotesque()

    def test_set_to_skip_empty1(self):
        """Setting elements to skip to None - should be the defaults"""
        toSkip = self._degrotesque._elements_to_skip
        self._degrotesque.set_to_skip(None)
        assert(self._degrotesque._elements_to_skip==toSkip)

    def test_set_to_skip_empty2(self):
        """Setting elements to skip to "" - should be the defaults"""
        toSkip = self._degrotesque._elements_to_skip
        self._degrotesque.set_to_skip("")
        assert(self._degrotesque._elements_to_skip==toSkip)

    def test_set_to_skip_single(self):
        """Setting a single element to skip"""
        self._degrotesque.set_to_skip("code")
        assert(self._degrotesque._elements_to_skip==["code"])

    def test_set_to_skip_multiple(self):
        """Setting a single elements to skip"""
        self._degrotesque.set_to_skip("code,test")
        assert(self._degrotesque._elements_to_skip==["code", "test"])

    def test_set_to_skip_falseDivider(self):
        """Trying to set an unknown action
        : todo Check whether the user should be warned if something like this occurs"""
        self._degrotesque.set_to_skip("code;test")
        assert(self._degrotesque._elements_to_skip==["code;test"])

