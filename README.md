[![License: BSD](https://img.shields.io/badge/License-BSD-green.svg)](https://github.com/dkrajzew/degrotesque/blob/master/LICENSE)
[![PyPI version](https://badge.fury.io/py/degrotesque.svg)](https://pypi.python.org/pypi/degrotesque)
![test](https://github.com/dkrajzew/degrotesque/actions/workflows/test.yml/badge.svg)
[![Downloads](https://pepy.tech/badge/degrotesque)](https://pepy.tech/project/degrotesque)
[![Downloads](https://static.pepy.tech/badge/degrotesque/week)](https://pepy.tech/project/degrotesque)
[![Coverage Status](https://coveralls.io/repos/github/dkrajzew/degrotesque/badge.svg?branch=main)](https://coveralls.io/github/dkrajzew/degrotesque?branch=main)
[![Documentation Status](https://readthedocs.org/projects/degrotesque/badge/?version=latest)](https://degrotesque.readthedocs.io/en/latest/?badge=latest)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=GVQQWZKB6FDES)


degrotesque &mdash; A web type setter.

Introduction
============

*degrotesque beautifies the web.*

**degrotesque** is a [Python](https://www.python.org/) script. It loads a text/markdown/HTML/XML file from the disc &mdash; or several in batch &mdash; and for each, it replaces some commonly used non-typographic characters, such as ", ', -, etc. into their typographic representation for improving the pages&apos; appearance.

E.g.:

 "Well - that's not what I had expected."

will become:

 &ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;

I think it looks __much__ better.

The starting and ending quotes have been replaced by &ldquo; and &rdquo;, respectively, the ' by &apos; and the - by an &mdash;. Of course, this script omits HTML-elements. It keeps the complete format as-is, and replaces characters by their proper HTML entity name or the respective unicode character.

It is meant to be a relatively **reliable post-processing step for web pages before releasing them**. In version 3.0.0 the support of markdown files was added.


Background
==========

I often write my texts and web pages using a plain editor. As such, the character " is always used for quotes, a dash is always a minus, etc.

I wanted to have a tool that automatically recognizes which characters should be replaced by their more typographic counterpart and applies the according rules.

I think it&rsquo;s a pity that major Desktop Publishing applications do this on the fly but many and even major web sites still show us plain ASCII characters.

**degrotesque** does the job pretty fine. After writing / building my pages, the tool converts them to a prettier and typographically more correct form. The structure and format of the pages is completely remained. And as said, it works reliable.

If you need any consultations, please let me know. If you know better, too.


Download and Installation
=========================

The __current version__ is [degrotesque-3.0.0](https://github.com/dkrajzew/degrotesque/releases/tag/3.0.0).

You may __install degrotesque__ using

```console
python -m pip install degrotesque
```

You may __download a copy or fork the code__ at [degrotesque&apos;s github page](https://github.com/dkrajzew/degrotesque).

Besides, you may __download the current release__ here:

* [degrotesque-3.0.0.zip](https://github.com/dkrajzew/degrotesque/archive/refs/tags/3.0.0.zip)
* [degrotesque-3.0.0.tar.gz](https://github.com/dkrajzew/degrotesque/archive/refs/tags/3.0.0.tar.gz)


License
=======

__degrotesque__ is licensed under [BSD license](LICENSE).

Documentation
=============

Usage
-----

__degrotesque__ is implemented in [Python](https://www.python.org/). It is started on the command line.

The option __-i _&lt;PATH&gt;___ / __--input _&lt;PATH&gt;___ tells the script which file(s) shall be read &mdash; you may name a file or a folder, here. If the option __-r__ / __--recursive__ is set, the given folder will be processed recursively.

The tool processes text files, HTML files, XML files, and their derivatives. Per default, all files are processed when **-i**  points to a folder. You may limit the files to process by their extension using the __-e _&lt;EXTENSION&gt;[,&lt;EXTENSION&gt;]\*___ / __--extensions _&lt;EXTENSION&gt;[,&lt;EXTENSION&gt;]*___ option. The files are assumed to be encoded using UTF-8 per default. You may change the encoding using the option __-E _&lt;ENCODING&gt;___ / __--encoding _&lt;ENCODING&gt;___.

The files are read one by one and the replacement of plain ASCII chars by some nicer ones is based upon a chosen set of &ldquo;actions&rdquo;. Known and default actions are given in [Appendix A](https://krajzewicz.de/docs/degrotesque/appendixA.html). You may select the actions to apply using the __-a _&lt;ACTION_NAME&gt;[,&lt;ACTION_NAME&gt;]*___ / __--actions _&lt;ACTION_NAME&gt;[,&lt;ACTION_NAME&gt;]\*___ option. The default actions are &#8216;_masks_&#8217;, &#8216;_quotes.english_&#8217;, &#8216;_dashes_&#8217;, &#8216;_ellipsis_&#8217;, &#8216;_math_&#8217;, &#8216;_apostrophe_&#8217;, and &#8216;_commercial_&#8217;.

Per default, Unicode entities are inserted (e.g. &#8216;&amp;#8211;&#8217; for an &#8216;&mdash;&#8217;). You may change this using the __--format _&lt;FORMAT&gt;___ / __-f _&lt;FORMAT&gt;___. The following formats are currently supported:

* &#8216;__unicode__&#8217;: uses numeric entities (e.g. &#8216;&amp;#8211;&#8217; for an &#8216;&mdash;&#8217;);
* &#8216;__html__&#8217;: uses HTML entities (e.g. &#8216;&amp;mdash;&#8217; for an &#8216;&mdash;&#8217;);
* &#8216;__text__&#8217;: uses plain (utf-8) characters (e.g. &#8216;—&#8217; for an &#8216;&mdash;&#8217;).


__degrotesque__ tries to determine whether the read files are plain text files, markdown files, or XML or HTML derivatives using the files&amp; extensions and contents. [Appendix B](https://krajzewicz.de/docs/degrotesque/appendixB.html) lists the extensions by which files are recognized as HTML / markdown files. To be secure, one may set __--html__ / __-H__ when processing HTML files, __--markdown__ / __-M__ when processing markdown files, or __--text__ / __-T__ when processing plain text files.

When parsing XML/HTML files, the script does not change the quotation marks within elements, of course. As well, the contents of several elements, such as &lt;code&gt; or &lt;pre&gt;, are skipped. You may change the list of elements which contents shall not be processed using the option __-s _&lt;ELEMENT_NAME&gt;[,&lt;ELEMENT_NAME&gt;]*___ / __--skip _&lt;ELEMENT_NAME&gt;[,&lt;ELEMENT_NAME&gt;]\*___. The list of elements that are skipped per default is given in [Appendix C](https://krajzewicz.de/docs/degrotesque/appendixC.html).

When parsing markdown files, code &mdash; both indented and defined using ` &mdash; is skipped. Quotes as well.

After the actions have been applied to its contents, the file is saved. By default, a backup of the original file is saved under the same name, with the appendix &ldquo;.orig&rdquo;. You may omit the creation of these backup files using the option __-B / --no-backup__.

The option __--help__ / __-h__ prints a help screen. The option __--version__ the __degrotesque&apos;s__ version number.

Please note that &ldquo;masks&rdquo; is a special action set that disallows the application of some other actions so that, e.g., the dividers in ISBN numbers are not replaced by &amp;ndash;. The masks action set is given in [Appendix D](https://krajzewicz.de/docs/degrotesque/appendixD.html).


Options
-------

The script can be started on the command line with the following options:

* __--input/-i _&lt;PATH&gt;___: the file or the folder to process
* __--recursive/-r__: Set if the folder &mdash; if given &mdash; shall be processed recursively
* __--extensions/-e _&lt;EXTENSION&gt;[,&lt;EXTENSION&gt;]*___: The extensions of files that shall be processed
* __--encoding/-E _&lt;ENCODING&gt;___: The assumed encoding of the files
* __--html/-H__: Files are HTML/XML-derivatives
* __--text/-T__: Files are plain text files
* __--markdown/-M__: Files are markdown files
* __--format/-f _&lt;FORMAT&gt;___: Define the format of the replacements [&#8216;_html_&#8217;, &#8216;_unicode_&#8217;, &#8216;_text_&#8217;]
* __--no-backup/-B__: Set if no backup files shall be generated
* __--skip/-s _&lt;ELEMENT_NAME&gt;[,&lt;ELEMENT_NAME&gt;]*___: Elements which contents shall not be changed
* __--actions/-a _&lt;ACTION_NAME&gt;[,&lt;ACTION_NAME&gt;]*___: Name the actions that shall be applied
* __--help__: Prints the help screen
* __--version__: Prints the version


Usage Examples
--------------

```console
degrotesque --input my_page.html --actions quotes.german
```

Replaces single and double quotes within the file &ldquo;my_page.html&rdquo; by their typographic German counterparts.

```console
degrotesque --input my_folder --recursive --no-backup
```

Applies the default actions to all files in the folder &ldquo;my_folder&rdquo; and all subfolders. No backup files are generated. The files format of each file is determined using the file&apos;s extension.

Application Programming Interface &mdash; API
---------------------------------------------

You may as well embedd __degrotesque__ within your own applications. The usage is very straightforward:
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

Further Documentation
---------------------

* The complete documentation is located at:
     * <https://degrotesque.readthedocs.io/en/latest/> and
     * <https://krajzewicz.de/docs/degrotesque/index.html>
* Discussions are open at <https://github.com/dkrajzew/degrotesque/discussions>
* The github repository is located at: <https://github.com/dkrajzew/degrotesque>
* The issue tracker is located at: <https://github.com/dkrajzew/degrotesque/issues>
* The PyPI page is located at: <https://pypi.org/project/degrotesque/>

Examples / Users
================

* My own pages (https://www.krajzewicz.de/).
* [PaletteWB](https://www.palettewb.com/) &mdash; a sophisticated palette editor for MS Windows.

Change Log
==========

degrotesque-3.0.0 (26.03.2023)
------------------------------

* Adding support for degrotesquing markdown files (contents of code and quotes are kept)
* Added support for processing plain text files; The distinction whether a file is a plain text file or a HTML/XML derivative is done using the extension (see Appendix B for used extensions) and by evaluating the contents; Everything is replaced in text files. When processing a file as a XML/HTML derivative, elements are skipped. Introducing the options __--text__ / __-T__, __--markdown__ / __-M__, and __--html__ / __-H__ to explicitly set the file type.
* Supporting different target encodings for the replacements using the __--format / -f _&lt;FORMAT&gt;___ option (the option __--unicode__ / __-u__ was removed):
    * &#8216;__unicode__&#8217;: uses numeric entities (e.g. &#8216;&amp;#8211;&#8217; for an &#8216;&mdash;&#8217;);
    * &#8216;__html__&#8217;: uses numeric entities (e.g. &#8216;&amp;mdash;&#8217; for an &#8216;&mdash;&#8217;);
    * &#8216;__text__&#8217;: uses plain (utf-8) characters (e.g. &#8216;—&#8217; for an &#8216;&mdash;&#8217;).
* 100 % test coverage :-)
* renamed master branch to main


degrotesque-2.0.6 (05.02.2023)
------------------------------

* Patched documentation (return types)
* Set proper formatting for [readthedocs](https://degrotesque.readthedocs.io/en/2.0.6/)
* It&apos;s not 2.0.4 due to caching by readthedocs


degrotesque-2.0.2 (04.02.2023)
------------------------------

* Corrected installation and execution as a console script


degrotesque-2.0 (05.01.2023)
----------------------------

* Changed the license to [BSD](https://github.com/dkrajzew/degrotesque/LICENSE).
* Using github actions for testing on push instead of using Travis CI
* Cleaned up project tree
* Adding an [mkdocs](https://www.mkdocs.org/) documentation

Older Versions
--------------

* see [ChangeLog](docs/mkdocs/changes.md)


Summary
=======

Well, have fun. If you have any comments / ideas / issues, please submit them to [degrotesque&apos;s issue tracker](https://github.com/dkrajzew/degrotesque/issues) on github or drop me a mail.

