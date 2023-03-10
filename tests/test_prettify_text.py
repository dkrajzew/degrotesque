# ===================================================================
# degrotesque - A web type setter.
#
# Tests for the prettify method
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
class TestDegrotesquePrettify(unittest.TestCase):
    """Testing the prettify method"""

    def setUp(self):
        self._degrotesque = degrotesque.Degrotesque()
        self._degrotesque.setFormat("html")

    def test_example(self):
        """The plain example test"""
        self._degrotesque._restoreDefaultActions()
        assert(self._degrotesque.prettify("\"Well - that's not what I had expected.\"", False)=="&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;")

    def test_example_between_elements(self):
        """Example embedded in a tag"""
        self._degrotesque._restoreDefaultActions()
        assert(self._degrotesque.prettify("<b>\"Well - that's not what I had expected.\"</b>", False)=="<b>&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;</b>")

    def test_example_in_pre(self):
        """Example in masked tag (pre)"""
        self._degrotesque._restoreDefaultActions()
        assert(self._degrotesque.prettify("<pre>\"Well - that's not what I had expected.\"</pre>", False)=="<pre>&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;</pre>")

    def test_action_quotes_english(self):
        """Testing 'quotes.english' action"""
        self._degrotesque.setActions("quotes.english")
        assert(self._degrotesque.prettify(" \"tests\" ", False)==" &ldquo;tests&rdquo; ")
        assert(self._degrotesque.prettify(" \'tests\' ", False)==" &lsquo;tests&rsquo; ")

    def test_action_quotes_german(self):
        """Testing 'quotes.german' action"""
        self._degrotesque.setActions("quotes.german")
        assert(self._degrotesque.prettify(" \"tests\" ", False)==" &bdquo;tests&rdquo; ")
        assert(self._degrotesque.prettify(" \'tests\' ", False)==" &sbquo;tests&rsquo; ")

    def test_action_quotes_french(self):
        """Testing 'quotes.french' action"""
        self._degrotesque.setActions("quotes.french")
        assert(self._degrotesque.prettify(" &lt;&lt;tests&gt;&gt; ", False)==" &laquo;tests&raquo; ")
        assert(self._degrotesque.prettify(" &lt;tests&gt; ", False)==" &lsaquo;tests&rsaquo; ")

    def test_action_to_quotes(self):
        """Testing 'to_quotes' action"""
        self._degrotesque.setActions("to_quotes")
        assert(self._degrotesque.prettify(" \"tests\" ", False)==" <q>tests</q> ")
        assert(self._degrotesque.prettify(" \'tests\' ", False)==" <q>tests</q> ")
        assert(self._degrotesque.prettify(" &lt;&lt;tests&gt;&gt; ", False)==" <q>tests</q> ")
        assert(self._degrotesque.prettify(" &lt;tests&gt; ", False)==" <q>tests</q> ")

    def test_action_commercial(self):
        """Testing 'commercial' action"""
        self._degrotesque.setActions("commercial")
        assert(self._degrotesque.prettify(" (c) ", False)==" &copy; ")
        assert(self._degrotesque.prettify(" (C) ", False)==" &copy; ")
        assert(self._degrotesque.prettify(" (r) ", False)==" &reg; ")
        assert(self._degrotesque.prettify(" (R) ", False)==" &reg; ")
        assert(self._degrotesque.prettify(" (tm) ", False)==" &trade; ")
        assert(self._degrotesque.prettify(" (TM) ", False)==" &trade; ")
        assert(self._degrotesque.prettify(" (tM) ", False)==" &trade; ")

    def test_action_dashes(self):
        """Testing 'dashes' action"""
        self._degrotesque.setActions("dashes")
        assert(self._degrotesque.prettify(" - ", False)==" &mdash; ")
        assert(self._degrotesque.prettify(u" 123-321 ", False)==u" 123&ndash;321 ")
        #assert(self._degrotesque.prettify(u" -321 ")==u" &ndash;321 ")
        #assert(self._degrotesque.prettify(u" 123- ")==u" 123&ndash; ")

    def test_action_bullets(self):
        """Testing 'bullets' action"""
        self._degrotesque.setActions("bullets")
        assert(self._degrotesque.prettify(" * ", False)==" &bull; ")

    def test_action_ellipsis(self):
        """Testing 'ellipsis' action"""
        self._degrotesque.setActions("ellipsis")
        assert(self._degrotesque.prettify(" ... ", False)==" &hellip; ")

    def test_action_apostrophe(self):
        """Testing 'apostrophe' action"""
        self._degrotesque.setActions("apostrophe")
        assert(self._degrotesque.prettify(" ' ", False)==" &apos; ")

    def test_action_math(self):
        """Testing 'math' action"""
        self._degrotesque.setActions("math")
        assert(self._degrotesque.prettify(" +/- ", False)==" &plusmn; ")
        assert(self._degrotesque.prettify(" 1/2 ", False)==" &frac12; ")
        assert(self._degrotesque.prettify(" 1/4 ", False)==" &frac14; ")
        assert(self._degrotesque.prettify(" ~ ", False)==" &asymp; ")
        assert(self._degrotesque.prettify(" != ", False)==" &ne; ")
        assert(self._degrotesque.prettify(" &lt;= ", False)==" &le; ")
        assert(self._degrotesque.prettify(" &gt;= ", False)==" &ge; ")
        assert(self._degrotesque.prettify(u" 123*321 ", False)==u" 123&times;321 ")
        assert(self._degrotesque.prettify(u" 123 * 321 ", False)==u" 123 &times; 321 ")
        assert(self._degrotesque.prettify(u" 123x321 ", False)==u" 123&times;321 ")
        assert(self._degrotesque.prettify(u" 123 x 321 ", False)==u" 123 &times; 321 ")
        assert(self._degrotesque.prettify(u" 123/321 ", False)==u" 123&divide;321 ")
        assert(self._degrotesque.prettify(u" 123 / 321 ", False)==u" 123 &divide; 321 ")

    def test_action_dagger(self):
        """Testing 'dagger' action"""
        self._degrotesque.setActions("dagger")
        assert(self._degrotesque.prettify(" ** ", False)==" &Dagger; ")
        assert(self._degrotesque.prettify(" * ", False)==" &dagger; ")

    def test_masks(self):
        """Testing masks
        todo: Think about minusses and dealing with numbers"""
        self._degrotesque.setActions("masks,dashes")
        assert(self._degrotesque.prettify(" ISSN 1001-1001 ", False)==" ISSN 1001-1001 ")
        assert(self._degrotesque.prettify(" ISBN 978-3-86680-192-9 ", False)==" ISBN 978-3-86680-192-9 ")
        assert(self._degrotesque.prettify(" ISBN 979-3-86680-192-9 ", False)==" ISBN 979-3-86680-192-9 ")
        #assert(self._degrotesque.prettify(" ISBN 978-3-86680-192 ", False)==" ISBN 978&ndash;3&ndash;86680&ndash;192 ")

    def test_action_chem(self):
        """Testing 'chem' action"""
        self._degrotesque.setActions("chem")
        assert(self._degrotesque.prettify("CO2", False)=="CO<sub>2</sub>")
        assert(self._degrotesque.prettify("C20H25N3O", False)=="C<sub>20</sub>H<sub>25</sub>N<sub>3</sub>O")

    def test_skip(self):
        """Testing whether skipping code works"""
        self._degrotesque.setActions("quotes.english")
        assert(self._degrotesque.prettify(" <script> if(i<0) echo \"a\"</script> \"Hello World\" ", False)==" <script> if(i<0) echo &ldquo;a&rdquo;</script> &ldquo;Hello World&rdquo; ")

    def test_attributes(self):
        """Testing whether skipping code works"""
        self._degrotesque.setActions("quotes.english")
        assert(self._degrotesque.prettify("\"<a href=\"test.html\">Hello World\"</a>\"", False)=="&ldquo;<a href=&rdquo;test.html&ldquo;>Hello World&rdquo;</a>\"")


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
    <code class=&ldquo;option&rdquo;>--css.attribute <em class=&ldquo;replaceable&rdquo;><code>&lt;NAME&gt;</code></em></code>
    sets the name of the written attribute, e.g. &ldquo;font-color&rdquo;. The default is
    &ldquo;<code class=&rdquo;constant&ldquo;>background-color</code>&rdquo;. The parameter <code class=&ldquo;option&rdquo;>--css.name
    <em class=&ldquo;replaceable&rdquo;><code>&lt;FORMAT_STRING&gt;</code></em></code> defines how the
    name of the entry is rendered. The parameter is a format string as
    described in detail below. The default is
    &ldquo;<code class=&rdquo;constant&ldquo;>.pal_%n_%i</code>&rdquo; &mdash; %n is replaced by the palette&apos;s name,
    &amp;i is replaced by the entry&apos;s index.</p>"""
        assert(self._degrotesque.prettify(text, False)==ctext)


    def test_prettify_toSkip_oddity(self):
        """Oddity#1"""
        self._degrotesque._restoreDefaultActions()
        self._degrotesque.setToSkip("(tm)")
        assert(self._degrotesque.prettify(" <(tm)>a</(tm)> ", False)==" <&trade;>a</&trade;> ")


