[![License: LGPL3](https://img.shields.io/badge/License-LGPL3-yellow.svg)](https://github.com/dkrajzew/degrotesque/blob/master/LICENSE.txt) 
[![PyPI version](https://badge.fury.io/py/degrotesque.svg)](https://pypi.python.org/pypi/degrotesque)
[![Travis CI](https://travis-ci.com/dkrajzew/degrotesque.svg?branch=master)](https://travis-ci.com/dkrajzew/degrotesque)

degrotesque - A tiny web type setter.

Introduction
============

The script loads a HTML page &mdash; or several in batch, one after the other &mdash; and for each, it replaces some commonly used non-typographic characters, such as ", ', -, etc. into their typographic representant for improving the pages&apos; appearance.  

E.g.:

 "Well - that's not what I had expected."

will become:

 &ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;

(Uhm, uhm, for those who don't see it, the starting and ending quotes have been replaced by &amp;ldquo; and &amp;rdquo;, respectively, the ' by &amp;apos; and the - by an &amp;mdash;.)

Download and Installation
=========================
The current version is [degrotesque-1.2](https://github.com/dkrajzew/degrotesque/releases/tag/degrotesque-1.2).

You may install __degrotesque__ using

```console
python -m pip install degrotesque
```

You may download a copy or fork the code at the [degrotesque&apos;s github page](https://github.com/dkrajzew/degrotesque).

Besides, you may download the current release [degrotesque-1.2](https://github.com/dkrajzew/degrotesque/releases/tag/degrotesque-1.2) here:
* [degrotesque-1.2.zip](https://github.com/dkrajzew/degrotesque/archive/degrotesque-1.2.zip)
* [degrotesque-1.2.tar.gz](https://github.com/dkrajzew/degrotesque/archive/degrotesque-1.2.tar.gz)

Licence
=======

__degrotesque__ is licensed under the [LGPL v3.0](LICENSE).

Documentation
=============

Usage
-----

__degrotesque__ is currently implemented in Python. It is started on the command line. The option __-i _&lt;PATH&gt;___ / __--input _&lt;PATH&gt;___ tells the script which file(s) shall be read — you may name a file or a folder, here. If the option __-r__ / __--recursive__ is set, the given folder will be processed recursively.

The tool processes only HTML-files and its derivatives. The extensions of those file types that are processed are given in Appendix A. But you may name the extensions of files to process using the __-e _&lt;EXTENSION&gt;[,&lt;EXTENSION&gt;]*___ / __--extensions _&lt;EXTENSION&gt;[,&lt;EXTENSION&gt;]*___ option.

The files are read one by one and the replacement of plain ASCII-chars by some nicer ones is based upon a chosen set of &ldquo;actions&rdquo;. Known and default actions are given in Appendix B. You may select the actions to apply using the __-a _&lt;ACTION_NAME&gt;[,&lt;ACTION_NAME&gt;]*___ / __--actions _&lt;ACTION_NAME&gt;[,&lt;ACTION_NAME&gt;]*___ option.

The files are assumed to be encoded as &ldquo;UTF-8&ldquo; per default. You may change the encoding using the option __-E _&lt;ENCODING&gt;___ / __--encoding _&lt;ENCODING&gt;___.

The script does not change the quotation marks of HTML elements, of course. As well, the contents of several elements, given in Appendix C are skipped. You may change the list of elements which contents shall not be processed using the option __-s _&lt;ELEMENT_NAME&gt;[,&lt;ELEMENT_NAME&gt;]*___ / __--skip _&lt;ELEMENT_NAME&gt;[,&lt;ELEMENT_NAME&gt;]*___. The default elements which contents are not processed are given in Appendix C.

After the actions have been applied to its contents, the file is saved. By default, the original file is saved under the same name, with the appendix &ldquo;.orig&rdquo;. You may omit the creation of these backup files using the option __-B / --no-backup__.

The default actions are: masks, quotes.english, dashes, ellipsis, math, apostroph. __Changes in version 1.2__: Please note that &ldquo;masks&rdquo; is a special action set that disallows the application of some other actions so that, e.g., the dividers in ISBN numbers are not replaced by &amp;ndash;. The masks actions set is given in Appendix D.

Options
-------

The script has the following options:
* __--input/-i _&lt;PATH&gt;___: the file or the folder to process
* __--encoding/-E _&lt;ENCODING&gt;___: The assumed encoding of the files
* __--recursive/-r__: Set if the folder &mdash; if given &mdash; shall be processed recursively
* __--no-backup/-B__: Set if no backup files shall be generated
* __--actions/-a _&lt;ACTION_NAME&gt;[,&lt;ACTION_NAME&gt;]*___: Name the actions that shall be applied
* __--extensions/-e _&lt;EXTENSION&gt;[,&lt;EXTENSION&gt;]*___: The extensions of files that shall be processed
* __--skip/-s _&lt;ELEMENT_NAME&gt;[,&lt;ELEMENT_NAME&gt;]*___: Elements which contents shall not be changed

Application Programming Interface - API
---------------------------------------

You may as well embedd __degrotesque__ within your own applications. The usage is very straightforward:
```console
import degrotesque
# build the degrotesque instance with default values
degrotesque = degrotesque.Degrotesque()
# apply degroteque
prettyString = degrotesque.prettify(uglyString)
```

The default values can be replaced using some of the class&apos; interfaces (methods):
```console
# change the actions to apply (by naming them)
# here: apply french quotes and math symbols
degrotesque.setActions("quotes.french,math")
# change the elements which contents shall be skipped
# here: skip the contents of "code", "script", and "style" elements
degrotesque.setToSkip("code,script,style")
```

You may as well consult the [degrotesque pydoc code documentation](http://www.krajzewicz.de/blog/degrotesque.html).

Further Documentation
---------------------

* The web page is located at: http://www.krajzewicz.de/blog/degrotesque.php
* The PyPI page is located at: https://pypi.org/project/degrotesque/
* The github repository is located at: https://github.com/dkrajzew/degrotesque
* The issue tracker is located at: https://github.com/dkrajzew/degrotesque/issues
* The Travis CI page is located at: https://travis-ci.com/github/dkrajzew/degrotesque
* The code documentation (pydoc) is located at: http://www.krajzewicz.de/blog/degrotesque.html

Implementation Notes
--------------------

* I tried [Genshi](https://genshi.edgewall.org/), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/), and [lxml](https://lxml.de/). All missed in keeping the code unchanged. So the parser just skips HTML-elements and the contents of some special elements, see above. Works in most cases.

Examples / Users
================

* my own pages (http://www.krajzewicz.de/).

ChangeLog
=========

version1.4
----------

* debugged the parser, had issues with script-sections at least

Summary
=======

Well, have fun. If you have any comments / ideas / issues, please submit them to [degrotesque's issue tracker](https://github.com/dkrajzew/degrotesque/issues) on github.

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

Please note that the actions are realised using regular expressions. I decided not to show them in the following for a better readability and show the visible changes only.

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


