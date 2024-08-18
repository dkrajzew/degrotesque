#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
"""degrotesque - Tests for the set_actions method."""
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


# --- test classes ------------------------------------------------------------
class TestDegrotesque_SetActions(unittest.TestCase):
    """Testing the set_actions method"""

    def setUp(self):
        self._degrotesque = degrotesque.Degrotesque()

    def test_set_actions_empty1(self):
        """Setting actions to None - should be the defaults"""
        self._degrotesque._restore_default_actions()
        actions = self._degrotesque._actions
        self._degrotesque.set_actions(None)
        assert(self._degrotesque._actions==actions)

    def test_set_actions_empty2(self):
        """Setting actions to "" - should be the defaults"""
        self._degrotesque._restore_default_actions()
        actions = self._degrotesque._actions
        self._degrotesque.set_actions("")
        assert(self._degrotesque._actions==actions)

    def test_set_actions_fromDB_single(self):
        """Setting single actions from the DB"""
        self._degrotesque._restore_default_actions()
        self._degrotesque.set_actions("quotes.english")
        assert(self._degrotesque._actions==degrotesque.actions_db["quotes.english"])
        self._degrotesque.set_actions("quotes.french")
        assert(self._degrotesque._actions==degrotesque.actions_db["quotes.french"])
        self._degrotesque.set_actions("quotes.german")
        assert(self._degrotesque._actions==degrotesque.actions_db["quotes.german"])
        self._degrotesque.set_actions("to_quotes")
        assert(self._degrotesque._actions==degrotesque.actions_db["to_quotes"])
        self._degrotesque.set_actions("commercial")
        assert(self._degrotesque._actions==degrotesque.actions_db["commercial"])
        self._degrotesque.set_actions("dashes")
        assert(self._degrotesque._actions==degrotesque.actions_db["dashes"])
        self._degrotesque.set_actions("bullets")
        assert(self._degrotesque._actions==degrotesque.actions_db["bullets"])
        self._degrotesque.set_actions("ellipsis")
        assert(self._degrotesque._actions==degrotesque.actions_db["ellipsis"])
        self._degrotesque.set_actions("apostrophe")
        assert(self._degrotesque._actions==degrotesque.actions_db["apostrophe"])
        self._degrotesque.set_actions("math")
        assert(self._degrotesque._actions==degrotesque.actions_db["math"])
        self._degrotesque.set_actions("dagger")
        assert(self._degrotesque._actions==degrotesque.actions_db["dagger"])

    def test_set_actions_fromDB_multiple(self):
        """Setting multiple actions from the DB"""
        self._degrotesque._restore_default_actions()
        self._degrotesque.set_actions("quotes.english,to_quotes")
        actions = []
        actions.extend(degrotesque.actions_db["quotes.english"])
        actions.extend(degrotesque.actions_db["to_quotes"])
        assert(self._degrotesque._actions==actions)

    def test_set_actions_unknown(self):
        """TRying to set an unknown action"""
        self._degrotesque._restore_default_actions()
        try:
            self._degrotesque.set_actions("xxx")
            assert False # pragma: no cover
        except ValueError as e:
            assert (type(e)==type(ValueError()))
            assert (str(e)=="Action 'xxx' is not known.")

    def test_set_actions_falseDivider(self):
        """Trying to set an unknown action"""
        self._degrotesque._restore_default_actions()
        try:
            self._degrotesque.set_actions("quotes.english;to_quotes")
            assert False # pragma: no cover
        except ValueError as e:
            assert (type(e)==type(ValueError()))
            assert (str(e)=="Action 'quotes.english;to_quotes' is not known.")

