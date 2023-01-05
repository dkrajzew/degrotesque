Embed in own Applications
=========================

You may as well embedd __degrotesque__ within your own applications. The usage is very straightforward:
```console
import degrotesque
# build the degrotesque instance with default values
degrotesque = degrotesque.Degrotesque()
# apply degroteque
prettyHTML = degrotesque.prettify(plainHTML)
```

The default values can be replaced using some of the class&apos; interfaces (methods):
```console
# change the actions to apply (by naming them)
# here: apply french quotes and math symbols
degrotesque.setActions("quotes.french,math")
# change the elements which contents shall be skipped
# here: skip the contents of "code",
#  "script", and "style" elements
degrotesque.setToSkip("code,script,style")
```

You may as well consult the [degrotesque pydoc code documentation](http://www.krajzewicz.de/blog/degrotesque.html).
