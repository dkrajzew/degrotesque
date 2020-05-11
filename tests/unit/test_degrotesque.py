"""test_degrotesque.py

Unittests for degrotesque, a tiny web type setter.

(c) Daniel Krajzewicz 2020
daniel@krajzewicz.de
http://www.krajzewicz.de
http://www.krajzewicz.de/blog/degrotesque.php

Available under GPL 3.0, all rights reserved
"""


# --- imports -------------------------------------------------------
import unittest
import degrotesque
from degrotesque import degrotesque



# --- classes -------------------------------------------------------
class TestDegrotesquePrettify(unittest.TestCase):
    """Testing the prettify method"""

    def setUp(self):
        self._degrotesque = degrotesque.Degrotesque()

    def test_example(self):
        """The plain example test"""
        assert(self._degrotesque.prettify("\"Well - that's not what I had expected.\"")=="&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;")
    
    def test_example_between_elements(self):
        """Example embedded in a tag"""
        assert(self._degrotesque.prettify("<b>\"Well - that's not what I had expected.\"</b>")=="<b>&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;</b>")
    
    def test_example_in_pre(self):
        """Example in masked tag (pre)"""
        assert(self._degrotesque.prettify("<pre>\"Well - that's not what I had expected.\"</pre>")=="<pre>\"Well - that's not what I had expected.\"</pre>")

    def test_action_quotes_english(self):
        """Testing 'quotes.english' action"""
        self._degrotesque.setActions("quotes.english")
        assert(self._degrotesque.prettify(" \"tests\" ")==" &ldquo;tests&rdquo; ")
        assert(self._degrotesque.prettify(" \'tests\' ")==" &lsquo;tests&rsquo; ")

    def test_action_quotes_german(self):
        """Testing 'quotes.german' action"""
        self._degrotesque.setActions("quotes.german")
        assert(self._degrotesque.prettify(" \"tests\" ")==" &bdquo;tests&rdquo; ")
        assert(self._degrotesque.prettify(" \'tests\' ")==" &sbquo;tests&rsquo; ")

    def test_action_quotes_french(self):
        """Testing 'quotes.french' action"""
        self._degrotesque.setActions("quotes.french")
        assert(self._degrotesque.prettify(" &lt;&lt;tests&gt;&gt; ")==" &laquo;tests&raquo; ")
        assert(self._degrotesque.prettify(" &lt;tests&gt; ")==" &lsaquo;tests&rsaquo; ")

    def test_action_to_quotes(self):
        """Testing 'to_quotes' action"""
        self._degrotesque.setActions("to_quotes")
        assert(self._degrotesque.prettify(" \"tests\" ")==" <q>tests</q> ")
        assert(self._degrotesque.prettify(" \'tests\' ")==" <q>tests</q> ")
        assert(self._degrotesque.prettify(" &lt;&lt;tests&gt;&gt; ")==" <q>tests</q> ")
        assert(self._degrotesque.prettify(" &lt;tests&gt; ")==" <q>tests</q> ")

    def test_action_commercial(self):
        """Testing 'commercial' action"""
        self._degrotesque.setActions("commercial")
        assert(self._degrotesque.prettify(" (c) ")==" &copy; ")
        assert(self._degrotesque.prettify(" (C) ")==" &copy; ")
        assert(self._degrotesque.prettify(" (r) ")==" &reg; ")
        assert(self._degrotesque.prettify(" (R) ")==" &reg; ")
        assert(self._degrotesque.prettify(" (tm) ")==" &trade; ")
        assert(self._degrotesque.prettify(" (TM) ")==" &trade; ")
        assert(self._degrotesque.prettify(" (tM) ")==" &trade; ")

    def test_action_dashes(self):
        """Testing 'dashes' action"""
        self._degrotesque.setActions("dashes")
        assert(self._degrotesque.prettify(" - ")==" &mdash; ")
        assert(self._degrotesque.prettify(u" 123-321 ")==u" 123&ndash;321 ")
        #assert(self._degrotesque.prettify(u" -321 ")==u" &ndash;321 ")
        #assert(self._degrotesque.prettify(u" 123- ")==u" 123&ndash; ")

    def test_action_bullets(self):
        """Testing 'bullets' action"""
        self._degrotesque.setActions("bullets")
        assert(self._degrotesque.prettify(" * ")==" &bull; ")

    def test_action_ellipsis(self):
        """Testing 'ellipsis' action"""
        self._degrotesque.setActions("ellipsis")
        assert(self._degrotesque.prettify(" ... ")==" &hellip; ")

    def test_action_apostrophe(self):
        """Testing 'apostrophe' action"""
        self._degrotesque.setActions("apostrophe")
        assert(self._degrotesque.prettify(" ' ")==" &apos; ")

    def test_action_math(self):
        """Testing 'math' action"""
        self._degrotesque.setActions("math")
        assert(self._degrotesque.prettify(" +/- ")==" &plusmn; ")
        assert(self._degrotesque.prettify(" 1/2 ")==" &frac12; ")
        assert(self._degrotesque.prettify(" 1/4 ")==" &frac14; ")
        assert(self._degrotesque.prettify(" ~ ")==" &asymp; ")
        assert(self._degrotesque.prettify(" != ")==" &ne; ")
        assert(self._degrotesque.prettify(" &lt;= ")==" &le; ")
        assert(self._degrotesque.prettify(" &gt;= ")==" &ge; ")
        assert(self._degrotesque.prettify(u" 123*321 ")==u" 123&times;321 ")
        assert(self._degrotesque.prettify(u" 123 * 321 ")==u" 123 &times; 321 ")
        assert(self._degrotesque.prettify(u" 123x321 ")==u" 123&times;321 ")
        assert(self._degrotesque.prettify(u" 123 x 321 ")==u" 123 &times; 321 ")
        assert(self._degrotesque.prettify(u" 123/321 ")==u" 123&divide;321 ")
        assert(self._degrotesque.prettify(u" 123 / 321 ")==u" 123 &divide; 321 ")

    def test_action_dagger(self):
        """Testing 'dagger' action"""
        self._degrotesque.setActions("dagger")
        assert(self._degrotesque.prettify(" ** ")==" &Dagger; ")
        assert(self._degrotesque.prettify(" * ")==" &dagger; ")



# --- methods -------------------------------------------------------
# -- main check
if __name__ == '__main__':
    unittest.main()

