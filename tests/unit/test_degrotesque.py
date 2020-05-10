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

    def test_example(self):
        """The plain example test"""
        assert(degrotesque.prettify("\"Well - that's not what I had expected.\"", degrotesque.getActions(None), degrotesque.getToSkip(None))=="&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;")
    
    def test_example_between_elements(self):
        """Example embedded in a tag"""
        assert(degrotesque.prettify("<b>\"Well - that's not what I had expected.\"</b>", degrotesque.getActions(None), degrotesque.getToSkip(None))=="<b>&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;</b>")
    
    def test_example_in_pre(self):
        """Example in masked tag (pre)"""
        assert(degrotesque.prettify("<pre>\"Well - that's not what I had expected.\"</pre>", degrotesque.getActions(None), degrotesque.getToSkip(None))=="<pre>\"Well - that's not what I had expected.\"</pre>")

    def test_action_quotes_english(self):
        """Testing 'quotes.english' action"""
        assert(degrotesque.prettify(" \"tests\" ", degrotesque.getActions("quotes.english"), degrotesque.getToSkip(None))==" &ldquo;tests&rdquo; ")
        assert(degrotesque.prettify(" \'tests\' ", degrotesque.getActions("quotes.english"), degrotesque.getToSkip(None))==" &lsquo;tests&rsquo; ")

    def test_action_quotes_german(self):
        """Testing 'quotes.german' action"""
        assert(degrotesque.prettify(" \"tests\" ", degrotesque.getActions("quotes.german"), degrotesque.getToSkip(None))==" &bdquo;tests&rdquo; ")
        assert(degrotesque.prettify(" \'tests\' ", degrotesque.getActions("quotes.german"), degrotesque.getToSkip(None))==" &sbquo;tests&rsquo; ")

    def test_action_quotes_french(self):
        """Testing 'quotes.french' action"""
        assert(degrotesque.prettify(" &lt;&lt;tests&gt;&gt; ", degrotesque.getActions("quotes.french"), degrotesque.getToSkip(None))==" &laquo;tests&raquo; ")
        assert(degrotesque.prettify(" &lt;tests&gt; ", degrotesque.getActions("quotes.french"), degrotesque.getToSkip(None))==" &lsaquo;tests&rsaquo; ")

    def test_action_to_quotes(self):
        """Testing 'to_quotes' action"""
        assert(degrotesque.prettify(" \"tests\" ", degrotesque.getActions("to_quotes"), degrotesque.getToSkip(None))==" <q>tests</q> ")
        assert(degrotesque.prettify(" \'tests\' ", degrotesque.getActions("to_quotes"), degrotesque.getToSkip(None))==" <q>tests</q> ")
        assert(degrotesque.prettify(" &lt;&lt;tests&gt;&gt; ", degrotesque.getActions("to_quotes"), degrotesque.getToSkip(None))==" <q>tests</q> ")
        assert(degrotesque.prettify(" &lt;tests&gt; ", degrotesque.getActions("to_quotes"), degrotesque.getToSkip(None))==" <q>tests</q> ")

    def test_action_commercial(self):
        """Testing 'commercial' action"""
        assert(degrotesque.prettify(" (c) ", degrotesque.getActions("commercial"), degrotesque.getToSkip(None))==" &copy; ")
        assert(degrotesque.prettify(" (C) ", degrotesque.getActions("commercial"), degrotesque.getToSkip(None))==" &copy; ")
        assert(degrotesque.prettify(" (r) ", degrotesque.getActions("commercial"), degrotesque.getToSkip(None))==" &reg; ")
        assert(degrotesque.prettify(" (R) ", degrotesque.getActions("commercial"), degrotesque.getToSkip(None))==" &reg; ")
        assert(degrotesque.prettify(" (tm) ", degrotesque.getActions("commercial"), degrotesque.getToSkip(None))==" &trade; ")
        assert(degrotesque.prettify(" (TM) ", degrotesque.getActions("commercial"), degrotesque.getToSkip(None))==" &trade; ")
        assert(degrotesque.prettify(" (tM) ", degrotesque.getActions("commercial"), degrotesque.getToSkip(None))==" &trade; ")

    def test_action_dashes(self):
        """Testing 'dashes' action"""
        assert(degrotesque.prettify(" - ", degrotesque.getActions("dashes"), degrotesque.getToSkip(None))==" &mdash; ")
        assert(degrotesque.prettify(u" 123-321 ", degrotesque.getActions("dashes"), degrotesque.getToSkip(None))==u" 123&ndash;321 ")
        assert(degrotesque.prettify(u" -321 ", degrotesque.getActions("dashes"), degrotesque.getToSkip(None))==u" &ndash;321 ")
        assert(degrotesque.prettify(u" 123- ", degrotesque.getActions("dashes"), degrotesque.getToSkip(None))==u" 123&ndash; ")

    def test_action_bullets(self):
        """Testing 'bullets' action"""
        assert(degrotesque.prettify(" * ", degrotesque.getActions("bullets"), degrotesque.getToSkip(None))==" &bull; ")

    def test_action_ellipsis(self):
        """Testing 'ellipsis' action"""
        assert(degrotesque.prettify(" ... ", degrotesque.getActions("ellipsis"), degrotesque.getToSkip(None))==" &hellip; ")

    def test_action_apostrophe(self):
        """Testing 'apostrophe' action"""
        assert(degrotesque.prettify(" ' ", degrotesque.getActions("apostrophe"), degrotesque.getToSkip(None))==" &apos; ")

    def test_action_math(self):
        """Testing 'math' action"""
        assert(degrotesque.prettify(" +/- ", degrotesque.getActions("math"), degrotesque.getToSkip(None))==" &plusmn; ")
        assert(degrotesque.prettify(" 1/2 ", degrotesque.getActions("math"), degrotesque.getToSkip(None))==" &frac12; ")
        assert(degrotesque.prettify(" 1/4 ", degrotesque.getActions("math"), degrotesque.getToSkip(None))==" &frac14; ")
        assert(degrotesque.prettify(" ~ ", degrotesque.getActions("math"), degrotesque.getToSkip(None))==" &asymp; ")
        assert(degrotesque.prettify(" != ", degrotesque.getActions("math"), degrotesque.getToSkip(None))==" &ne; ")
        assert(degrotesque.prettify(" &lt;= ", degrotesque.getActions("math"), degrotesque.getToSkip(None))==" &le; ")
        assert(degrotesque.prettify(" &gt;= ", degrotesque.getActions("math"), degrotesque.getToSkip(None))==" &ge; ")
        assert(degrotesque.prettify(u" 123*321 ", degrotesque.getActions("math"), degrotesque.getToSkip(None))==u" 123&times;321 ")
        assert(degrotesque.prettify(u" 123 * 321 ", degrotesque.getActions("math"), degrotesque.getToSkip(None))==u" 123 &times; 321 ")
        assert(degrotesque.prettify(u" 123x321 ", degrotesque.getActions("math"), degrotesque.getToSkip(None))==u" 123&times;321 ")
        assert(degrotesque.prettify(u" 123 x 321 ", degrotesque.getActions("math"), degrotesque.getToSkip(None))==u" 123 &times; 321 ")
        assert(degrotesque.prettify(u" 123/321 ", degrotesque.getActions("math"), degrotesque.getToSkip(None))==u" 123&divide;321 ")
        assert(degrotesque.prettify(u" 123 / 321 ", degrotesque.getActions("math"), degrotesque.getToSkip(None))==u" 123 &divide; 321 ")

    def test_action_dagger(self):
        """Testing 'dagger' action"""
        assert(degrotesque.prettify(" ** ", degrotesque.getActions("dagger"), degrotesque.getToSkip(None))==" &Dagger; ")
        assert(degrotesque.prettify(" * ", degrotesque.getActions("dagger"), degrotesque.getToSkip(None))==" &dagger; ")



# --- methods -------------------------------------------------------
# -- main check
if __name__ == '__main__':
    unittest.main()

