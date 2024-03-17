#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
"""degrotesque - Tests for the prettify method using HTML entities."""
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
from degrotesque import degrotesque
from degrotesque import marker_html


# --- test classes ------------------------------------------------------------
class TestDegrotesque_Prettify_HTML(unittest.TestCase):
    """Testing the prettify method"""

    def setUp(self):
        self._degrotesque = degrotesque.Degrotesque()
        self._degrotesque.set_format("html")
        self._marker = marker_html.DegrotesqueHTMLMarker()

    def test_example(self):
        """The plain example test"""
        self._degrotesque._restore_default_actions()
        assert(self._degrotesque.prettify("\"Well - that's not what I had expected.\"", self._marker)=="&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;")

    def test_example_between_elements(self):
        """Example embedded in a tag"""
        self._degrotesque._restore_default_actions()
        assert(self._degrotesque.prettify("<b>\"Well - that's not what I had expected.\"</b>", self._marker)=="<b>&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;</b>")

    def test_example_in_pre(self):
        """Example in masked tag (pre)"""
        self._degrotesque._restore_default_actions()
        assert(self._degrotesque.prettify("<pre>\"Well - that's not what I had expected.\"</pre>", self._marker)=="<pre>\"Well - that's not what I had expected.\"</pre>")

    def test_action_quotes_english(self):
        """Testing 'quotes.english' action"""
        self._degrotesque.set_actions("quotes.english")
        assert(self._degrotesque.prettify(" \"tests\" ", self._marker)==" &ldquo;tests&rdquo; ")
        assert(self._degrotesque.prettify(" \'tests\' ", self._marker)==" &lsquo;tests&rsquo; ")

    def test_action_quotes_german(self):
        """Testing 'quotes.german' action"""
        self._degrotesque.set_actions("quotes.german")
        assert(self._degrotesque.prettify(" \"tests\" ", self._marker)==" &bdquo;tests&rdquo; ")
        assert(self._degrotesque.prettify(" \'tests\' ", self._marker)==" &sbquo;tests&rsquo; ")

    def test_action_quotes_french(self):
        """Testing 'quotes.french' action"""
        self._degrotesque.set_actions("quotes.french")
        assert(self._degrotesque.prettify(" &lt;&lt;tests&gt;&gt; ", self._marker)==" &laquo;tests&raquo; ")
        assert(self._degrotesque.prettify(" &lt;tests&gt; ", self._marker)==" &lsaquo;tests&rsaquo; ")

    def test_action_to_quotes(self):
        """Testing 'to_quotes' action"""
        self._degrotesque.set_actions("to_quotes")
        assert(self._degrotesque.prettify(" \"tests\" ", self._marker)==" <q>tests</q> ")
        assert(self._degrotesque.prettify(" \'tests\' ", self._marker)==" <q>tests</q> ")
        assert(self._degrotesque.prettify(" &lt;&lt;tests&gt;&gt; ", self._marker)==" <q>tests</q> ")
        assert(self._degrotesque.prettify(" &lt;tests&gt; ", self._marker)==" <q>tests</q> ")

    def test_action_commercial(self):
        """Testing 'commercial' action"""
        self._degrotesque.set_actions("commercial")
        assert(self._degrotesque.prettify(" (c) ", self._marker)==" &copy; ")
        assert(self._degrotesque.prettify(" (C) ", self._marker)==" &copy; ")
        assert(self._degrotesque.prettify(" (r) ", self._marker)==" &reg; ")
        assert(self._degrotesque.prettify(" (R) ", self._marker)==" &reg; ")
        assert(self._degrotesque.prettify(" (tm) ", self._marker)==" &trade; ")
        assert(self._degrotesque.prettify(" (TM) ", self._marker)==" &trade; ")
        assert(self._degrotesque.prettify(" (tM) ", self._marker)==" &trade; ")

    def test_action_dashes(self):
        """Testing 'dashes' action"""
        self._degrotesque.set_actions("dashes")
        assert(self._degrotesque.prettify(" - ", self._marker)==" &mdash; ")
        assert(self._degrotesque.prettify(u" 123-321 ", self._marker)==u" 123&ndash;321 ")
        #assert(self._degrotesque.prettify(u" -321 ")==u" &ndash;321 ")
        #assert(self._degrotesque.prettify(u" 123- ")==u" 123&ndash; ")

    def test_action_bullets(self):
        """Testing 'bullets' action"""
        self._degrotesque.set_actions("bullets")
        assert(self._degrotesque.prettify(" * ", self._marker)==" &bull; ")

    def test_action_ellipsis(self):
        """Testing 'ellipsis' action"""
        self._degrotesque.set_actions("ellipsis")
        assert(self._degrotesque.prettify(" ... ", self._marker)==" &hellip; ")

    def test_action_apostrophe(self):
        """Testing 'apostrophe' action"""
        self._degrotesque.set_actions("apostrophe")
        assert(self._degrotesque.prettify(" ' ", self._marker)==" &apos; ")

    def test_action_math(self):
        """Testing 'math' action"""
        self._degrotesque.set_actions("math")
        assert(self._degrotesque.prettify(" +/- ", self._marker)==" &plusmn; ")
        assert(self._degrotesque.prettify(" 1/2 ", self._marker)==" &frac12; ")
        assert(self._degrotesque.prettify(" 1/4 ", self._marker)==" &frac14; ")
        assert(self._degrotesque.prettify(" ~ ", self._marker)==" &asymp; ")
        assert(self._degrotesque.prettify(" != ", self._marker)==" &ne; ")
        assert(self._degrotesque.prettify(" &lt;= ", self._marker)==" &le; ")
        assert(self._degrotesque.prettify(" &gt;= ", self._marker)==" &ge; ")
        assert(self._degrotesque.prettify(u" 123*321 ", self._marker)==u" 123&times;321 ")
        assert(self._degrotesque.prettify(u" 123 * 321 ", self._marker)==u" 123 &times; 321 ")
        assert(self._degrotesque.prettify(u" 123x321 ", self._marker)==u" 123&times;321 ")
        assert(self._degrotesque.prettify(u" 123 x 321 ", self._marker)==u" 123 &times; 321 ")
        assert(self._degrotesque.prettify(u" 123/321 ", self._marker)==u" 123&divide;321 ")
        assert(self._degrotesque.prettify(u" 123 / 321 ", self._marker)==u" 123 &divide; 321 ")

    def test_action_dagger(self):
        """Testing 'dagger' action"""
        self._degrotesque.set_actions("dagger")
        assert(self._degrotesque.prettify(" ** ", self._marker)==" &Dagger; ")
        assert(self._degrotesque.prettify(" * ", self._marker)==" &dagger; ")

    def test_masks(self):
        """Testing masks
        todo: Think about minusses and dealing with numbers"""
        self._degrotesque.set_actions("masks,dashes")
        assert(self._degrotesque.prettify(" ISSN 1001-1001 ", self._marker)==" ISSN 1001-1001 ")
        assert(self._degrotesque.prettify(" ISBN 978-3-86680-192-9 ", self._marker)==" ISBN 978-3-86680-192-9 ")
        assert(self._degrotesque.prettify(" ISBN 979-3-86680-192-9 ", self._marker)==" ISBN 979-3-86680-192-9 ")
        #assert(self._degrotesque.prettify(" ISBN 978-3-86680-192 ", True)==" ISBN 978&ndash;3&ndash;86680&ndash;192 ")

    def test_action_chem(self):
        """Testing 'chem' action"""
        self._degrotesque.set_actions("chem")
        assert(self._degrotesque.prettify("CO2", self._marker)=="CO<sub>2</sub>")
        assert(self._degrotesque.prettify("C20H25N3O", self._marker)=="C<sub>20</sub>H<sub>25</sub>N<sub>3</sub>O")

    def test_skip(self):
        """Testing whether skipping code works"""
        self._degrotesque.set_actions("quotes.english")
        assert(self._degrotesque.prettify(" <script> if(i<0) echo \"a\"</script> \"Hello World\" ", self._marker)==" <script> if(i<0) echo \"a\"</script> &ldquo;Hello World&rdquo; ")

    def test_attributes(self):
        """Testing whether skipping code works"""
        self._degrotesque.set_actions("quotes.english")
        assert(self._degrotesque.prettify("\"<a href=\"test.html\">Hello World\"</a>\"", self._marker)=="&ldquo;<a href=\"test.html\">Hello World&rdquo;</a>\"")


    def test_real1(self):
        """A previously failing real-life example"""
        self._degrotesque._restore_default_actions()
        text = """<p>The rendering of .css-tables can be altered as well. The parameter
    <code class="option">--css.attribute <em class="replaceable"><code>&lt;NAME&gt;</code></em></code>
    sets the name of the written attribute, e.g. "font-color". The default is
    "<code class="constant">background-color</code>". The parameter <code class="option">--css.name
    <em class="replaceable"><code>&lt;FORMAT_STRING&gt;</code></em></code> defines how the
    name of the entry is rendered. The parameter is a format string as
    described in detail below. The default is
    "<code class="constant">.pal_%n_%i</code>" - %n is replaced by the palette's name,
    &amp;i is replaced by the entry's index.</p>"""
        ctext = """<p>The rendering of .css-tables can be altered as well. The parameter
    <code class="option">--css.attribute <em class="replaceable"><code>&lt;NAME&gt;</code></em></code>
    sets the name of the written attribute, e.g. &ldquo;font-color&rdquo;. The default is
    &ldquo;<code class="constant">background-color</code>&rdquo;. The parameter <code class="option">--css.name
    <em class="replaceable"><code>&lt;FORMAT_STRING&gt;</code></em></code> defines how the
    name of the entry is rendered. The parameter is a format string as
    described in detail below. The default is
    &ldquo;<code class="constant">.pal_%n_%i</code>&rdquo; &mdash; %n is replaced by the palette&apos;s name,
    &amp;i is replaced by the entry&apos;s index.</p>"""
        assert(self._degrotesque.prettify(text, self._marker)==ctext)


    def test_prettify_toSkip_oddity(self):
        """Oddity#1"""
        self._degrotesque._restore_default_actions()
        self._degrotesque.set_to_skip("(tm)")
        assert(self._degrotesque.prettify(" <(tm)>a</(tm)> ", self._marker)==" <(tm)>a</(tm)> ")


