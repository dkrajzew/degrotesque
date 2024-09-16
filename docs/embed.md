# Embed in own Applications

Besides running __degrotesque__ on the [command line](./cmd.md), you may as well 
embed __degrotesque__ within your own applications. There are two ways to do this:

* Functional by calling the [prettify](./api_degrotesque.md#src.degrotesque.prettify) function
from the module;
* Using a [Degrotesque](./api_degrotesque.md#src.degrotesque.Degrotesque) instance and use it's [prettify](./api_degrotesque.md#src.degrotesque.Degrotesque.prettify) method.

When __degrotesque__ shall be called only once, the first method is more convenient.
The second should be used when processing multiple files of the same type. 

## Functional

Assuming you have a text snippet, just apply the [prettify](./api_degrotesque.md#src.degrotesque.prettify) method on it:

```python
import degrotesque
ugly_str = "Well - that's not what I had expected."
nice_str = degrotesque.prettify(ugly_str)
```

The function is defined as:

```python
prettify(document, marker=None, actions=None, 
		 replacement_format='text', to_skip=None)
```

with the following parameters:

* __document__: the original document;
* __marker__: Either a string that names which marker to use or the marker object to use; the following names are known:
	* &#8216;__sgml__&#8217;: used for processing XML/HTML documents;
	* &#8216;__text__&#8217;: used for processing plain text files;
	* &#8216;__md__&#8217;: used for processing Markdown documents;
	* &#8216;__doxygen__&#8217;: used for processing files documents using the Doxygen syntax;
	* &#8216;__python__&#8217;: used for processing Python files;
	* &#8216;__rst__&#8217;: used for processing restructuredText documents.
* __replacement_format__: How the inserted character shall be represented with:
	* &#8216;__unicode__&#8217;: uses numeric entities (e.g. &#8216;&amp;#8211;&#8217; for an &#8216;&mdash;&#8217;);
	* &#8216;__html__&#8217;: uses HTML entities (e.g. &#8216;&amp;mdash;&#8217; for an &#8216;&mdash;&#8217;);
	* &#8216;__char__&#8217;: uses plain (utf-8) characters (e.g. &#8216;—&#8217; for an &#8216;&mdash;&#8217;).
* __to_skip__: a list of names of the elements that contents shall be skipped; works only when processing SGML/XML/HTML-documents; when None is given, the default elements to skip are used, see [Appendix C)[./appendixC.md).

[prettify](./api_degrotesque.md#src.degrotesque.prettify) returns the converted document contents.


## Using a Degrotesque object

When processing multiple documents the same way, using an instance with pre-set options
should be faster. An basic example is:

```python
import degrotesque
# build the degrotesque instance with default values
my_prettifyier = degrotesque.Degrotesque()
# apply degroteque
ugly_str = "Well - that's not what I had expected."
nice_str = my_prettifyier.prettify(ugly_str)
```




The default values can be replaced using some of the class&apos; interfaces (methods):
```python
# change the actions to apply (by naming them)
# here: apply french quotes and math symbols
degrotesque.setActions("quotes.french,math")
# change the elements which contents shall be skipped
# here: skip the contents of "code",
#  "script", and "style" elements
degrotesque.setToSkip("code,script,style")
```

## Further information

You may consult the [degrotesque pydoc code documentation](http://www.krajzewicz.de/blog/degrotesque.html).
