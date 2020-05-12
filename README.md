[![License: GPL3](https://img.shields.io/badge/License-GPL3-yellow.svg)](https://github.com/dkrajzew/degrotesque/blob/master/LICENSE.txt) [![PyPI version](https://badge.fury.io/py/degrotesque.svg)](https://pypi.python.org/pypi/prov2bigchaindb)

degrotesque - A tiny web type setter

Introduction
============

The script loads a HTML page &mdash; or several in batch, one after the other &mdash; and for each, it replaces some commonly used non-typographic characters, such as ", ', -, etc. into their typographic representant for improving the pages&apos; appearance.  

E.g.:

 "Well - that's not what I had expected."

will become:

 &ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;

(Uhm, uhm, for those who don't see it, the starting and ending quotes have been replaced by &amp;ldquo; and &amp;rdquo;, respectively, the ' by &amp;apos; and the - by an &amp;mdash;.)

Documentation
=============

Usage
-----

__degrotesque__ is currently implemented in Python. It is started on the command line. The option __-i _&lt;PATH&gt;___ / __--input _&lt;PATH&gt;___ tells the script which file(s) shall be read — you may name a file or a folder, here. If the option __-r__ / __--recursive__ is set, the given folder will be processed recursively.

The tool processes only HTML-files and its derivatives. The extensions of those file types that are processed are given in Appendix A. But you may name the extensions of files to process using the __-e _&lt;EXTENSION&gt;[,&lt;EXTENSION&gt;]*___ / __--extensions _&lt;EXTENSION&gt;[,&lt;EXTENSION&gt;]*___ option.

The files are read one by one and the replacement of plain ASCII-chars by some nicer ones is based upon a chosen set of “actions”. Known and default actions are given in Appendix B. You may select the actions to apply using the __-a _&lt;ACTION_NAME&gt;[,&lt;ACTION_NAME&gt;]*___ / __--actions _&lt;ACTION_NAME&gt;[,&lt;ACTION_NAME&gt;]*___ option.

The files are assumed to be encoded as "UTF-8" per default. You may change the encoding using the option __-E _&lt;ENCODING&gt;___ / __--encoding _&lt;ENCODING&gt;___.

The script does not change the quotation marks of HTML elements, of course. As well, the contents of several elements, given in Appendix C are skipped. You may change the list of elements which contents shall not be processed using the option __-s _&lt;ELEMENT_NAME&gt;[,&lt;ELEMENT_NAME&gt;]*___ / __--skip _&lt;ELEMENT_NAME&gt;[,&lt;ELEMENT_NAME&gt;]*___.

After the actions have been applied to its contents, the file is saved. By default, the original file is saved under the same name, with the appendix “.orig”. You may omit the creation of these backup files using the option __-B / --no-backup__.



Options
-------

The script has the following options:
* --input/-i: the file or the folder to process
* --encoding/-E: The assumed encoding of the files
* --recursive/-r: Set if the folder - if given - shall be processed recursively
* --no-backup/-B: Set if no backup files shall be generated
* --actions/-a: Name the actions that shall be applied
* --extensions/-e: The extensions of files that shall be processed
* --skip/-s: Elements which contents shall not be changed

All of the text is replaced. This means everything not within a &lt; and a &gt;. But yes, the script is smart enough to skip the contents of the elements "pre", "style", "script", "code", and "<?".

The default actions are: quotes.english, dashes, ellipsis, math, apostroph. The list of all implemented actions is given below, as well as the default extensions of files that will be passed if a folder is given.

There are some caveats, yes:
* If you embed HTML code in HTML (not suported by HTML, but who cares), it may yield in odd behaviour.
* If you have php-pages and combine php-generated and plain HTML text, it may yield in odd behaviour. Etc. So you should check your pages for correctness after applying degrotesque.

degrotesque is licensed under the [GPL v3.0](LICENSE.txt).

You may install it using
python -m pip install degrotesque

Documentation:
* The web page is located at: http://www.krajzewicz.de/blog/degrotesque.php
* The PyPI page is located at: https://pypi.org/project/degrotesque/


Well, have fun. If you have any questions or comments, let me know.

Named Actions
-------------

The following action sets are currently implemented. 

| Action Name | From Opening String | From Closing String | To Opening String | To Closing String |
| ---- | ---- | ---- | ---- | ---- |
| quotes.english | " '" | "'" | " &lsquo;" | "&rsquo;" |
| | "\"" | "\"" | "&ldquo;" | "&rdquo;" |
| quotes.french | "&lt;" | "&gt;" | "&lsaquo;" | "&rsaquo;" |
| | "&lt;&lt;" | "&gt;&gt;" | "&laquo;" | "&raquo;" |
| quotes.german | " '" | "'" | " &sbquo;" | "&rsquo;" |
| | "\"" | "\"" | "&bdquo;" | "&rdquo;" |
| to_quotes | " '" | "'" | " &lt;q&gt;" | "&lt;/q&gt;" |
| | "\"" | "\"" | "&lt;q&gt;" | "&lt;/q&gt;" |
| | "&lt;&lt;" | "&gt;&gt;" | "&lt;q&gt;" | "&lt;/q&gt;" |
| commercial | "(c)" | | "&copy;" | |
| | "(C)" | | "&copy;" | |
| | "(r)" | | "&reg;" | |
| | "(R)" | | "&reg;" | |
| | "(tm)" | | "&trade;" | |
| | "(TM)" | | "&trade;" | |
| dashes | " - " | | "&mdash;" | |
| bullets | "*" | | "&bull;" | |
| ellipsis | "..." | | "&hellip;" | |
| apostrophe | "'" | | "&apos;" | |
| math | "+/-" | | "&plusmn;" | |
| | "1/2" | | "&frac12;" | |
| | "1/4" | | "&frac14;" | |
| | "~" | | "&asymp;" | |
| | "!=" | | "&ne;" | |
| | "<=" | | "&le;" | |
| | ">=" | | "&ge;" | |
| dagger | "**" | | "&Dagger;" | |
| | "*" | | "&dagger;" | |
 
Default Extensions
------------------

Files with the following extensions are parsed per default:
* html, htm, xhtml,
* php, phtml, phtm, php2, php3, php4, php5,
* asp, 
* jsp, jspx, 
* shtml, shtm, sht, stm,
* vbhtml,
* ppthtml,   
* ssp, jhtml
 
Notes
-----
* I tried [Genshi](https://genshi.edgewall.org/), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/), and [lxml](https://lxml.de/). All missed in keeping the code unchanged. So the parser just skips HTML-elements and the contents of some special elements, see above. Works in most cases.



