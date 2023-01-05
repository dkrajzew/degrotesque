[![License: BSD](https://img.shields.io/badge/License-BSD-green.svg)](https://github.com/dkrajzew/degrotesque/blob/master/LICENSE) 
[![PyPI version](https://badge.fury.io/py/degrotesque.svg)](https://pypi.python.org/pypi/degrotesque)
![test](https://github.com/dkrajzew/degrotesque/actions/workflows/test.yml/badge.svg)
[![Downloads](https://pepy.tech/badge/degrotesque)](https://pepy.tech/project/degrotesque)
[![Coverage](https://img.shields.io/badge/coverage-98%25-success)](https://img.shields.io/badge/coverage-98%25-success)


degrotesque &mdash; A web type setter.

Introduction
============

_degrotesque beautifies the web._

__degrotesque__ is a [Python](https://www.python.org/) script. It loads an HTML file from the disc — or several in batch, one after the other — and for each, it replaces some commonly used non-typographic characters, such as ", ', -, etc. into their typographic representant for improving the pages&apos; appearance.  

E.g.:

 "Well - that's not what I had expected."

will become:

 &ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;

I think, it looks __much__ better.

The starting and ending quotes have been replaced by &ldquo; and &rdquo;, respectively, the ' by &apos; and the - by an &mdash;. Of course, this script omits HTML-elements. It keeps the complete format as-is, and replaces characters by their proper HTML entity name or the respective unicode character. 

It is meant to be a relatively reliable post-processing step for web pages before releasing them.


Background
==========

I often write my texts and web pages using a plain editor. As such, the character " is always used for quotes, a dash is always a minus, etc.

I wanted to have a tool that automatically recognizes which characters should be replaced by their more typographic counterpart and applies the according rules. 

I think it's a pity that major Desktop Publishing applications do this on the fly but many and even major web sites still show us plain ASCII characters.

**degrotesque** does the job pretty fine. After writing / building my pages, the tool converts them to a prettier and typographically more correct form. The structure and format of the pages is completely remained. And as said, it works reliable.

If you need any consultations, please let me know. If you know better, too.


Download and Installation
=========================
The __current version__ is [degrotesque-2.0](https://github.com/dkrajzew/degrotesque/releases/tag/2.0). You may __install degrotesque__ using

```console
python -m pip install degrotesque
```

You may __download a copy or fork the code__ at [degrotesque&apos;s github page](https://github.com/dkrajzew/degrotesque). Besides, you may __download the current release__ here:

* [degrotesque-2.0.zip](https://github.com/dkrajzew/degrotesque/archive/refs/tags/2.0.zip)
* [degrotesque-2.0.tar.gz](https://github.com/dkrajzew/degrotesque/archive/refs/tags/2.0.tar.gz)


License
=======

__degrotesque__ is licensed under [BSD license](LICENSE).

Documentation
=============

Usage
-----

__degrotesque__ is implemented in [Python](https://www.python.org/). It is started on the command line.

The option __-i _&lt;PATH&gt;___ / __--input _&lt;PATH&gt;___ tells the script which file(s) shall be read &mdash; you may name a file or a folder, here. If the option __-r__ / __--recursive__ is set, the given folder will be processed recursively.

The tool processes HTML files, XML files, and their derivatives. The extensions of file types that are processed are given in Appendix A. You may change the extensions of files to process using the __-e _&lt;EXTENSION&gt;[,&lt;EXTENSION&gt;]*___ / __--extensions _&lt;EXTENSION&gt;[,&lt;EXTENSION&gt;]*___ option.

The files are read one by one and the replacement of plain ASCII chars by some nicer ones is based upon a chosen set of &ldquo;actions&rdquo;. Known and default actions are given in Appendix B. You may select the actions to apply using the __-a _&lt;ACTION_NAME&gt;[,&lt;ACTION_NAME&gt;]*___ / __--actions _&lt;ACTION_NAME&gt;[,&lt;ACTION_NAME&gt;]*___ option. The default actions are ___masks___, ___quotes.english___, ___dashes___, ___ellipsis___, ___math___, ___apostrophe___, and ___commercial___. Per default, HTML entities are inserted. If you rather wish to have unicode values, use the option __-u__ / __--unicode__.

The files are assumed to be encoded using UTF-8 per default. You may change the encoding using the option __-E _&lt;ENCODING&gt;___ / __--encoding _&lt;ENCODING&gt;___.

The script does not change the quotation marks of HTML elements, of course. As well, the contents of several elements, such as &lt;code&gt; or &lt;pre&gt;, are skipped. You may change the list of elements which contents shall not be processed using the option __-s _&lt;ELEMENT_NAME&gt;[,&lt;ELEMENT_NAME&gt;]*___ / __--skip _&lt;ELEMENT_NAME&gt;[,&lt;ELEMENT_NAME&gt;]*___. The list of elements that are skipped per default is given in Appendix C.

After the actions have been applied to its contents, the file is saved. By default, a backup of the original file is saved under the same name, with the appendix &ldquo;.orig&rdquo;. You may omit the creation of these backup files using the option __-B / --no-backup__.

Please note that &ldquo;masks&rdquo; is a special action set that disallows the application of some other actions so that, e.g., the dividers in ISBN numbers are not replaced by &amp;ndash;. The masks action set is given in Appendix D.

Options
-------

The script has the following options:
* __--input/-i _&lt;PATH&gt;___: the file or the folder to process
* __--recursive/-r__: Set if the folder &mdash; if given &mdash; shall be processed recursively
* __--no-backup/-B__: Set if no backup files shall be generated
* __--unicode/-u__: When set, unicode characters instead of HTML-entities are used
* __--extensions/-e _&lt;EXTENSION&gt;[,&lt;EXTENSION&gt;]*___: The extensions of files that shall be processed
* __--encoding/-E _&lt;ENCODING&gt;___: The assumed encoding of the files
* __--skip/-s _&lt;ELEMENT_NAME&gt;[,&lt;ELEMENT_NAME&gt;]*___: Elements which contents shall not be changed
* __--actions/-a _&lt;ACTION_NAME&gt;[,&lt;ACTION_NAME&gt;]*___: Name the actions that shall be applied
* __--help__: Prints the help screen

Usage Examples
--------------

```console
degrotesque -i my_page.html -a quotes.german
```

Replaces single and double quotes within the file "my_page.html" by their typographic German counterparts.

```console
degrotesque -i my_folder -r --no-backup
```

Applies the default actions to all files that match the extension in the folder "my_folder" and all subfolders. No backup files are generated.

Application Programming Interface - API
---------------------------------------

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

Further Documentation
---------------------

* The github repository is located at: https://github.com/dkrajzew/degrotesque
* The issue tracker is located at: https://github.com/dkrajzew/degrotesque/issues
* The PyPI page is located at: https://pypi.org/project/degrotesque/
* The code documentation (pydoc) is located at: http://www.krajzewicz.de/blog/degrotesque.html
* A web page is located at: http://www.krajzewicz.de/blog/degrotesque.php

Implementation Notes
--------------------

* I tried [Genshi](https://genshi.edgewall.org/), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/), and [lxml](https://lxml.de/). All missed in keeping the code unchanged. So the parser just skips HTML-elements and the contents of some special elements, see above. Works in most cases.

Examples / Users
================

* My own pages (https://www.krajzewicz.de/).
* [PaletteWB](https://www.palettewb.com/) &mdash; a sophisticated palette editor for MS Windows.

Change Log
==========

Version 2.0 (to come)
------------------------

* Changed the license to [BSD](LICENSE).
* Using github actions for testing on push instead of using Travis CI
* Cleaned up project tree

Older Versions
--------------

* see [ChangeLog](docs/CHANGES.md)


Summary
=======

Well, have fun. If you have any comments / ideas / issues, please submit them to [degrotesque's issue tracker](https://github.com/dkrajzew/degrotesque/issues) on github or drop me a mail.

Appendices
==========

Appendix A: Default Extensions
------------------------------

Files with the following extensions are parsed per default:
* html, htm, xhtml,
* php, phtml, phtm, php2, php3, php4, php5,
* asp,
* jsp, jspx,
* shtml, shtm, sht, stm,
* vbhtml,
* ppthtml,
* ssp, jhtml

Appendix B: Named Actions
-------------------------

The following action sets are currently implemented.

Please note that the actions are realized using regular expressions. I decided not to show them in the following for a better readability and show the visible changes only.

| Action Name | From Opening String | From Closing String | To Opening String | To Closing String |
| ---- | ---- | ---- | ---- | ---- |
| quotes.english | ' | ' | &lsquo; | &rsquo; |
| | " | " | &ldquo; | &rdquo; |
| quotes.french | &lt; | &gt; | &lsaquo; | &rsaquo; |
| | &lt;&lt; | &gt;&gt; | &laquo; | &raquo; |
| quotes.german | ' | ' | &sbquo; | &rsquo; |
| | " | " | &bdquo; | &rdquo; |
| to_quotes | ' | ' | &lt;q&gt; | &lt;/q&gt; |
| | " | " | &lt;q&gt; | &lt;/q&gt; |
| | &lt;&lt; | &gt;&gt; | &lt;q&gt; | &lt;/q&gt; |
| | &lt; | &gt; | &lt;q&gt; | &lt;/q&gt; |
| commercial | (c) | | &copy; | |
| | (r) | | &reg; | |
| | (tm) | | &trade; | |
| dashes |  -  | | &mdash; | |
| | &lt;NUMBER&gt;-&lt;NUMBER&gt; | | &lt;NUMBER&gt;&ndash;&lt;NUMBER&gt; | |
| bullets | * | | &bull; | |
| ellipsis | ... | | &hellip; | |
| apostrophe | ' | | &apos; | |
| math | +/- | | &plusmn; | |
| | 1/2 | | &frac12; | |
| | 1/4 | | &frac14; | |
| | 3/4 | | &frac34; | |
| | ~ | | &asymp; | |
| | != | | &ne; | |
| | &lt;= | | &le; | |
| | &gt;= | | &ge; | |
| | &lt;NUMBER&gt;\*&lt;NUMBER&gt; | | &lt;NUMBER&gt;&times;&lt;NUMBER&gt; | |
| | &lt;NUMBER&gt;x&lt;NUMBER&gt; | | &lt;NUMBER&gt;&times;&lt;NUMBER&gt; | |
| | &lt;NUMBER&gt;/&lt;NUMBER&gt; | | &lt;NUMBER&gt;&divide;&lt;NUMBER&gt; | |
| dagger | ** | | &Dagger; | |
| | * | | &dagger; | |
 
Appendix C: Skipped Elements
----------------------------

The contents of the following elements are not processed by default:
* script
* code
* style
* pre
* ?
* ?php
* %
* %=
* %@
* %--
* %!
* !--

Appendix D: Masking Action Set
------------------------------

The &ldquo;masks&rdquo; action set is masking some patterns to avoid replacements. When matching, the matching string is kept. The actions are given in the following. Please note that the numbers in { } brackets give the number of subsequent elements.

* 978-&lt;NUMBER&gt;-&lt;NUMBER&gt;-&lt;NUMBER&gt;-&lt;NUMBER&gt;{1}&lt;NO_NUMBER&gt;: avoid ISBN replacement
* 979-&lt;NUMBER&gt;-&lt;NUMBER&gt;-&lt;NUMBER&gt;-&lt;NUMBER&gt;{1}&lt;NO_NUMBER&gt;: avoid ISBN replacement
* &lt;NUMBER&gt;-&lt;NUMBER&gt;-&lt;NUMBER&gt;-&lt;NUMBER&gt;{1}&lt;NO_NUMBER&gt;: avoid ISBN replacement
* ISSN &lt;NUMBER&gt;{4}-&lt;NUMBER&gt;{4}: avoid ISSN replacement

&copy; Daniel Krajzewicz 2020&ndash;2023

