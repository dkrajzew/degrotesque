"""degrotesque.py

A tiny web type setter.

Tests for the setToSkip method.

(c) Daniel Krajzewicz 2020-2022
daniel@krajzewicz.de
http://www.krajzewicz.de
https://github.com/dkrajzew/degrotesque
http://www.krajzewicz.de/blog/degrotesque.php

Available under LGPL 3 or later, all rights reserved
"""


# --- imports -------------------------------------------------------
import unittest
from degrotesque import degrotesque



# --- classes -------------------------------------------------------
class TestDegrotesqueSetToSkip(unittest.TestCase):
    """Testing the setToSkip method"""

    def setUp(self):
        self._degrotesque = degrotesque.Degrotesque()

    def test_setToSkip_empty1(self):
        """Setting elements to skip to None - should be the defaults"""
        toSkip = self._degrotesque._elementsToSkip
        self._degrotesque.setToSkip(None)
        assert(self._degrotesque._elementsToSkip==toSkip)
    
    def test_setToSkip_empty2(self):
        """Setting elements to skip to "" - should be the defaults"""
        toSkip = self._degrotesque._elementsToSkip
        self._degrotesque.setToSkip(None)
        assert(self._degrotesque._elementsToSkip==toSkip)
    
    def test_setToSkip_single(self):
        """Setting a single element to skip"""
        self._degrotesque.setToSkip("code")
        assert(self._degrotesque._elementsToSkip==["code"])

    def test_setToSkip_multiple(self):
        """Setting a single elements to skip"""
        self._degrotesque.setToSkip("code,test")
        assert(self._degrotesque._elementsToSkip==["code", "test"])

    def test_setToSkip_falseDivider(self):
        """Trying to set an unknown action
        : todo Check whether the user should be warned if something like this occurs"""
        self._degrotesque.setToSkip("code;test")
        assert(self._degrotesque._elementsToSkip==["code;test"])
