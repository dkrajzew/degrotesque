import unittest
import degrotesque
from degrotesque import degrotesque



class TestDegrotesquePrettify(unittest.TestCase):
    def test_example(self):
        """The plain example test"""
        assert(degrotesque.prettify("\"Well - that's not what I had expected.\"", degrotesque.getActions(None))=="&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;")
    
    def test_example_between_elements(self):
        """Example embedded in a tag"""
        assert(degrotesque.prettify("<b>\"Well - that's not what I had expected.\"</b>", degrotesque.getActions(None))=="<b>&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;</b>")
    
    def test_example_in_pre(self):
        """Example in masked tag (pre)"""
        assert(degrotesque.prettify("<pre>\"Well - that's not what I had expected.\"</pre>", degrotesque.getActions(None))=="<pre>\"Well - that's not what I had expected.\"</pre>")

    def test_action_quotes_english(self):
        """Testing 'quotes.english' action"""
        assert(degrotesque.prettify(" \"tests\" ", degrotesque.getActions("quotes.english"))==" &ldquo;tests&rdquo; ")
        assert(degrotesque.prettify(" \'tests\' ", degrotesque.getActions("quotes.english"))==" &lsquo;tests&rsquo; ")

    def test_action_quotes_german(self):
        """Testing 'quotes.german' action"""
        assert(degrotesque.prettify(" \"tests\" ", degrotesque.getActions("quotes.german"))==" &bdquo;tests&rdquo; ")
        assert(degrotesque.prettify(" \'tests\' ", degrotesque.getActions("quotes.german"))==" &sbquo;tests&rsquo; ")

    def test_action_quotes_french(self):
        """Testing 'quotes.french' action"""
        assert(degrotesque.prettify(" &lt;&lt;tests&gt;&gt; ", degrotesque.getActions("quotes.french"))==" &laquo;tests&raquo; ")
        assert(degrotesque.prettify(" &lt;tests&gt; ", degrotesque.getActions("quotes.french"))==" &lsaquo;tests&rsaquo; ")

    def test_action_to_quotes(self):
        """Testing 'to_quotes' action"""
        assert(degrotesque.prettify(" \"tests\" ", degrotesque.getActions("to_quotes"))==" <q>tests</q> ")
        assert(degrotesque.prettify(" \'tests\' ", degrotesque.getActions("to_quotes"))==" <q>tests</q> ")
        assert(degrotesque.prettify(" &lt;&lt;tests&gt;&gt; ", degrotesque.getActions("to_quotes"))==" <q>tests</q> ")
        assert(degrotesque.prettify(" &lt;tests&gt; ", degrotesque.getActions("to_quotes"))==" <q>tests</q> ")

    def test_action_commercial(self):
        """Testing 'commercial' action"""
        assert(degrotesque.prettify(" (c) ", degrotesque.getActions("commercial"))==" &copy; ")
        assert(degrotesque.prettify(" (C) ", degrotesque.getActions("commercial"))==" &copy; ")
        assert(degrotesque.prettify(" (r) ", degrotesque.getActions("commercial"))==" &reg; ")
        assert(degrotesque.prettify(" (R) ", degrotesque.getActions("commercial"))==" &reg; ")
        assert(degrotesque.prettify(" (tm) ", degrotesque.getActions("commercial"))==" &trade; ")
        assert(degrotesque.prettify(" (TM) ", degrotesque.getActions("commercial"))==" &trade; ")
        assert(degrotesque.prettify(" (tM) ", degrotesque.getActions("commercial"))==" &trade; ")

    def test_action_dashes(self):
        """Testing 'dashes' action"""
        assert(degrotesque.prettify(" - ", degrotesque.getActions("dashes"))==" &mdash; ")
        assert(degrotesque.prettify(u" 123-321 ", degrotesque.getActions("dashes"))==u" 123&ndash;321 ")
        assert(degrotesque.prettify(u" -321 ", degrotesque.getActions("dashes"))==u" &ndash;321 ")
        assert(degrotesque.prettify(u" 123- ", degrotesque.getActions("dashes"))==u" 123&ndash; ")

    def test_action_bullets(self):
        """Testing 'bullets' action"""
        assert(degrotesque.prettify(" * ", degrotesque.getActions("bullets"))==" &bull; ")

    def test_action_ellipsis(self):
        """Testing 'ellipsis' action"""
        assert(degrotesque.prettify(" ... ", degrotesque.getActions("ellipsis"))==" &hellip; ")

    def test_action_apostrophe(self):
        """Testing 'apostrophe' action"""
        assert(degrotesque.prettify(" ' ", degrotesque.getActions("apostrophe"))==" &apos; ")

    def test_action_math(self):
        """Testing 'math' action"""
        assert(degrotesque.prettify(" +/- ", degrotesque.getActions("math"))==" &plusmn; ")
        assert(degrotesque.prettify(" 1/2 ", degrotesque.getActions("math"))==" &frac12; ")
        assert(degrotesque.prettify(" 1/4 ", degrotesque.getActions("math"))==" &frac14; ")
        assert(degrotesque.prettify(" ~ ", degrotesque.getActions("math"))==" &asymp; ")
        assert(degrotesque.prettify(" != ", degrotesque.getActions("math"))==" &ne; ")
        assert(degrotesque.prettify(" &lt;= ", degrotesque.getActions("math"))==" &le; ")
        assert(degrotesque.prettify(" &gt;= ", degrotesque.getActions("math"))==" &ge; ")
        assert(degrotesque.prettify(u" 123*321 ", degrotesque.getActions("math"))==u" 123&times;321 ")
        assert(degrotesque.prettify(u" 123 * 321 ", degrotesque.getActions("math"))==u" 123 &times; 321 ")
        assert(degrotesque.prettify(u" 123x321 ", degrotesque.getActions("math"))==u" 123&times;321 ")
        assert(degrotesque.prettify(u" 123 x 321 ", degrotesque.getActions("math"))==u" 123 &times; 321 ")
        assert(degrotesque.prettify(u" 123/321 ", degrotesque.getActions("math"))==u" 123&divide;321 ")
        assert(degrotesque.prettify(u" 123 / 321 ", degrotesque.getActions("math"))==u" 123 &divide; 321 ")

    def test_action_dagger(self):
        """Testing 'dagger' action"""
        assert(degrotesque.prettify(" ** ", degrotesque.getActions("dagger"))==" &Dagger; ")
        assert(degrotesque.prettify(" * ", degrotesque.getActions("dagger"))==" &dagger; ")




if __name__ == '__main__':
    unittest.main()

