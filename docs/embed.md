Embed in own Applications
=========================

You may as well embed __degrotesque__ within your own applications. The usage is very straightforward:

```python
import degrotesque
# build the degrotesque instance with default values
degrotesque = degrotesque.Degrotesque()
# apply degroteque
plain = ' <script> if(i<0) echo "a"</script> "Hello World" '
pretty = degrotesque.prettify(plain, True)
plain = ' <script> if(i<0) echo "a"</script> "Hello World" '
pretty = degrotesque.prettify(plain, False)
```

The first call will deliver:

```console
 <script> if(i<0) echo "a"</script> &ldquo;Hello World&rdquo;
```

while the second &mdash; as the string is interpreted as plain text, not HTML will deliver:

```console
 <script> if(i<0) echo &ldquo;a&rdquo;</script> &ldquo;Hello World&rdquo;
```

what is probably not what you wished.



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

You may as well consult the [degrotesque pydoc code documentation](http://www.krajzewicz.de/blog/degrotesque.html).
