# ===================================================================
# degrotesque - A web type setter.
#
# Tests for the prettify method
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
class TestDegrotesquePrettify(unittest.TestCase):
    """Testing the prettify method"""

    def setUp(self):
        self._degrotesque = degrotesque.Degrotesque()
        self._degrotesque.setFormat("unicode")

    def test_example(self):
        """The plain example test"""
        self._degrotesque._restoreDefaultActions()
        assert(self._degrotesque.prettify("\"Well - that's not what I had expected.\"", True)=="&#8220;Well &#8212; that&#39;s not what I had expected.&#8221;")

    def test_example_between_elements(self):
        """Example embedded in a tag"""
        self._degrotesque._restoreDefaultActions()
        assert(self._degrotesque.prettify("<b>\"Well - that's not what I had expected.\"</b>", True)=="<b>&#8220;Well &#8212; that&#39;s not what I had expected.&#8221;</b>")

    def test_example_in_pre(self):
        """Example in masked tag (pre)"""
        self._degrotesque._restoreDefaultActions()
        assert(self._degrotesque.prettify("<pre>\"Well - that's not what I had expected.\"</pre>", True)=="<pre>\"Well - that's not what I had expected.\"</pre>")

    def test_action_quotes_english(self):
        """Testing 'quotes.english' action"""
        self._degrotesque.setActions("quotes.english")
        assert(self._degrotesque.prettify(" \"tests\" ", True)==" &#8220;tests&#8221; ")
        assert(self._degrotesque.prettify(" \'tests\' ", True)==" &#8216;tests&#8217; ")

    def test_action_quotes_german(self):
        """Testing 'quotes.german' action"""
        self._degrotesque.setActions("quotes.german")
        assert(self._degrotesque.prettify(" \"tests\" ", True)==" &#x201E;tests&#x201D; ")
        assert(self._degrotesque.prettify(" \'tests\' ", True)==" &#x201A;tests&#x2019; ")

    def test_action_quotes_french(self):
        """Testing 'quotes.french' action"""
        self._degrotesque.setActions("quotes.french")
        assert(self._degrotesque.prettify(" &lt;&lt;tests&gt;&gt; ", True)==" &#x00AB;tests&#x00BB; ")
        assert(self._degrotesque.prettify(" &lt;tests&gt; ", True)==" &#x2039;tests&#x203A; ")

    def test_action_to_quotes(self):
        """Testing 'to_quotes' action"""
        self._degrotesque.setActions("to_quotes")
        assert(self._degrotesque.prettify(" \"tests\" ", True)==" <q>tests</q> ")
        assert(self._degrotesque.prettify(" \'tests\' ", True)==" <q>tests</q> ")
        assert(self._degrotesque.prettify(" &lt;&lt;tests&gt;&gt; ", True)==" <q>tests</q> ")
        assert(self._degrotesque.prettify(" &lt;tests&gt; ", True)==" <q>tests</q> ")

    def test_action_commercial(self):
        """Testing 'commercial' action"""
        self._degrotesque.setActions("commercial")
        assert(self._degrotesque.prettify(" (c) ", True)==" &#169; ")
        assert(self._degrotesque.prettify(" (C) ", True)==" &#169; ")
        assert(self._degrotesque.prettify(" (r) ", True)==" &#174; ")
        assert(self._degrotesque.prettify(" (R) ", True)==" &#174; ")
        assert(self._degrotesque.prettify(" (tm) ", True)==" &#8482; ")
        assert(self._degrotesque.prettify(" (TM) ", True)==" &#8482; ")
        assert(self._degrotesque.prettify(" (tM) ", True)==" &#8482; ")

    def test_action_dashes(self):
        """Testing 'dashes' action"""
        self._degrotesque.setActions("dashes")
        assert(self._degrotesque.prettify(" - ", True)==" &#8212; ")
        assert(self._degrotesque.prettify(u" 123-321 ", True)==u" 123&#8211;321 ")
        #assert(self._degrotesque.prettify(u" -321 ")==u" &#8211;321 ")
        #assert(self._degrotesque.prettify(u" 123- ")==u" 123&#8211; ")

    def test_action_bullets(self):
        """Testing 'bullets' action"""
        self._degrotesque.setActions("bullets")
        assert(self._degrotesque.prettify(" * ", True)==" &#8226; ")

    def test_action_ellipsis(self):
        """Testing 'ellipsis' action"""
        self._degrotesque.setActions("ellipsis")
        assert(self._degrotesque.prettify(" ... ", True)==" &#8230; ")

    def test_action_apostrophe(self):
        """Testing 'apostrophe' action"""
        self._degrotesque.setActions("apostrophe")
        assert(self._degrotesque.prettify(" ' ", True)==" &#39; ")

    def test_action_math(self):
        """Testing 'math' action"""
        self._degrotesque.setActions("math")
        assert(self._degrotesque.prettify(" +/- ", True)==" &#177; ")
        assert(self._degrotesque.prettify(" 1/2 ", True)==" &#189; ")
        assert(self._degrotesque.prettify(" 1/4 ", True)==" &#188; ")
        assert(self._degrotesque.prettify(" ~ ", True)==" &#8776; ")
        assert(self._degrotesque.prettify(" != ", True)==" &#8800; ")
        assert(self._degrotesque.prettify(" &lt;= ", True)==" &#8804; ")
        assert(self._degrotesque.prettify(" &gt;= ", True)==" &#8805; ")
        assert(self._degrotesque.prettify(u" 123*321 ", True)==u" 123&#215;321 ")
        assert(self._degrotesque.prettify(u" 123 * 321 ", True)==u" 123 &#215; 321 ")
        assert(self._degrotesque.prettify(u" 123x321 ", True)==u" 123&#215;321 ")
        assert(self._degrotesque.prettify(u" 123 x 321 ", True)==u" 123 &#215; 321 ")
        assert(self._degrotesque.prettify(u" 123/321 ", True)==u" 123&#247;321 ")
        assert(self._degrotesque.prettify(u" 123 / 321 ", True)==u" 123 &#247; 321 ")

    def test_action_dagger(self):
        """Testing 'dagger' action"""
        self._degrotesque.setActions("dagger")
        assert(self._degrotesque.prettify(" ** ", True)==" &#8225; ")
        assert(self._degrotesque.prettify(" * ", True)==" &#8224; ")

    def test_masks(self):
        """Testing masks
        todo: Think about minusses and dealing with numbers"""
        self._degrotesque.setActions("masks,dashes")
        assert(self._degrotesque.prettify(" ISSN 1001-1001 ", True)==" ISSN 1001-1001 ")
        assert(self._degrotesque.prettify(" ISBN 978-3-86680-192-9 ", True)==" ISBN 978-3-86680-192-9 ")
        assert(self._degrotesque.prettify(" ISBN 979-3-86680-192-9 ", True)==" ISBN 979-3-86680-192-9 ")
        #assert(self._degrotesque.prettify(" ISBN 978-3-86680-192 ")==" ISBN 978&#8211;3&#8211;86680&#8211;192 ")

    def test_action_chem(self):
        """Testing 'chem' action"""
        self._degrotesque.setActions("chem")
        assert(self._degrotesque.prettify("CO2", True)=="CO<sub>2</sub>")
        assert(self._degrotesque.prettify("C20H25N3O", True)=="C<sub>20</sub>H<sub>25</sub>N<sub>3</sub>O")

    def test_skip(self):
        """Testing whether skipping code works"""
        self._degrotesque.setActions("quotes.english")
        assert(self._degrotesque.prettify(" <script> if(i<0) echo \"a\"</script> \"Hello World\" ", True)==" <script> if(i<0) echo \"a\"</script> &#8220;Hello World&#8221; ")

    def test_attributes(self):
        """Testing whether skipping code works"""
        self._degrotesque.setActions("quotes.english")
        assert(self._degrotesque.prettify("\"<a href=\"test.html\">Hello World\"</a>\"", True)=="&#8220;<a href=\"test.html\">Hello World&#8221;</a>\"")


    def test_real1(self):
        """A previously failing real-life example"""
        self._degrotesque._restoreDefaultActions()
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
    sets the name of the written attribute, e.g. &#8220;font-color&#8221;. The default is
    &#8220;<code class="constant">background-color</code>&#8221;. The parameter <code class="option">--css.name
    <em class="replaceable"><code>&lt;FORMAT_STRING&gt;</code></em></code> defines how the
    name of the entry is rendered. The parameter is a format string as
    described in detail below. The default is
    &#8220;<code class="constant">.pal_%n_%i</code>&#8221; &#8212; %n is replaced by the palette&#39;s name,
    &amp;i is replaced by the entry&#39;s index.</p>"""
        assert(self._degrotesque.prettify(text, True)==ctext)


    def test_prettify_toSkip_oddity(self):
        """Oddity#1"""
        self._degrotesque._restoreDefaultActions()
        self._degrotesque.setToSkip("(tm)")
        assert(self._degrotesque.prettify(" <(tm)>a</(tm)> ", True)==" <(tm)>a</(tm)> ")

