# ===================================================================
# degrotesque - A web type setter.
# Version 2.0.
#
# Tests for the setActions method
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
class TestDegrotesqueSetActions(unittest.TestCase):
    """Testing the setActions method"""

    def setUp(self):
        self._degrotesque = degrotesque.Degrotesque()

    def test_setActions_empty1(self):
        """Setting actions to None - should be the defaults"""
        self._degrotesque._restoreDefaultActions()
        actions = self._degrotesque._actions
        self._degrotesque.setActions(None)
        assert(self._degrotesque._actions==actions)
    
    def test_setActions_empty2(self):
        """Setting actions to "" - should be the defaults"""
        self._degrotesque._restoreDefaultActions()
        actions = self._degrotesque._actions
        self._degrotesque.setActions("")
        assert(self._degrotesque._actions==actions)
    
    def test_setActions_fromDB_single(self):
        """Setting single actions from the DB"""
        self._degrotesque._restoreDefaultActions()
        self._degrotesque.setActions("quotes.english")
        assert(self._degrotesque._actions==degrotesque.actionsDB["quotes.english"])
        self._degrotesque.setActions("quotes.french")
        assert(self._degrotesque._actions==degrotesque.actionsDB["quotes.french"])
        self._degrotesque.setActions("quotes.german")
        assert(self._degrotesque._actions==degrotesque.actionsDB["quotes.german"])
        self._degrotesque.setActions("to_quotes")
        assert(self._degrotesque._actions==degrotesque.actionsDB["to_quotes"])
        self._degrotesque.setActions("commercial")
        assert(self._degrotesque._actions==degrotesque.actionsDB["commercial"])
        self._degrotesque.setActions("dashes")
        assert(self._degrotesque._actions==degrotesque.actionsDB["dashes"])
        self._degrotesque.setActions("bullets")
        assert(self._degrotesque._actions==degrotesque.actionsDB["bullets"])
        self._degrotesque.setActions("ellipsis")
        assert(self._degrotesque._actions==degrotesque.actionsDB["ellipsis"])
        self._degrotesque.setActions("apostrophe")
        assert(self._degrotesque._actions==degrotesque.actionsDB["apostrophe"])
        self._degrotesque.setActions("math")
        assert(self._degrotesque._actions==degrotesque.actionsDB["math"])
        self._degrotesque.setActions("dagger")
        assert(self._degrotesque._actions==degrotesque.actionsDB["dagger"])
        self._degrotesque.setActions("masks")
        assert(self._degrotesque._actions==degrotesque.actionsDB["masks"])
    
    def test_setActions_fromDB_multiple(self):
        """Setting multiple actions from the DB"""
        self._degrotesque._restoreDefaultActions()
        self._degrotesque.setActions("quotes.english,to_quotes")
        actions = []
        actions.extend(degrotesque.actionsDB["quotes.english"])
        actions.extend(degrotesque.actionsDB["to_quotes"])
        assert(self._degrotesque._actions==actions)

    def test_setActions_unknown(self):
        """TRying to set an unknown action"""
        self._degrotesque._restoreDefaultActions()
        try:
            self._degrotesque.setActions("xxx")
            assert False
        except ValueError as e:
            assert (type(e)==type(ValueError()))
            assert (str(e)=="Action 'xxx' is not known.")

    def test_setActions_falseDivider(self):
        """Trying to set an unknown action"""
        self._degrotesque._restoreDefaultActions()
        try:
            self._degrotesque.setActions("quotes.english;to_quotes")
            assert False
        except ValueError as e:
            assert (type(e)==type(ValueError()))
            assert (str(e)=="Action 'quotes.english;to_quotes' is not known.")

