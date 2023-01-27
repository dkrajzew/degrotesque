Running on the Command Line
===========================

__degrotesque__ is implemented in [Python](https://www.python.org/). It is started on the command line.


Description
-----------

The option __-i _&lt;PATH&gt;___ / __--input _&lt;PATH&gt;___ tells the script which file(s) shall be read &mdash; you may name a file or a folder, here. If the option __-r__ / __--recursive__ is set, the given folder will be processed recursively.

The tool processes HTML files, XML files, and their derivatives. The extensions of file types that are processed are given in [Appendix A](appendixA.md). You may change the extensions of files to process using the __-e _&lt;EXTENSION&gt;[,&lt;EXTENSION&gt;]\*___ / __--extensions _&lt;EXTENSION&gt;[,&lt;EXTENSION&gt;]*___ option.

The files are read one by one and the replacement of plain ASCII chars by some nicer ones is based upon a chosen set of &ldquo;actions&rdquo;. Known and default actions are given in [Appendix B](appendixB.md). You may select the actions to apply using the __-a _&lt;ACTION_NAME&gt;[,&lt;ACTION_NAME&gt;]*___ / __--actions _&lt;ACTION_NAME&gt;[,&lt;ACTION_NAME&gt;]\*___ option. The default actions are ___masks___, ___quotes.english___, ___dashes___, ___ellipsis___, ___math___, ___apostrophe___, and ___commercial___. Per default, HTML entities are inserted. If you rather wish to have unicode values, use the option __-u__ / __--unicode__.

The files are assumed to be encoded using UTF-8 per default. You may change the encoding using the option __-E _&lt;ENCODING&gt;___ / __--encoding _&lt;ENCODING&gt;___.

The script does not change the quotation marks of HTML elements, of course. As well, the contents of several elements, such as &lt;code&gt; or &lt;pre&gt;, are skipped. You may change the list of elements which contents shall not be processed using the option __-s _&lt;ELEMENT_NAME&gt;[,&lt;ELEMENT_NAME&gt;]*___ / __--skip _&lt;ELEMENT_NAME&gt;[,&lt;ELEMENT_NAME&gt;]\*___. The list of elements that are skipped per default is given in [Appendix C](appendixC.md).

After the actions have been applied to its contents, the file is saved. By default, a backup of the original file is saved under the same name, with the appendix &ldquo;.orig&rdquo;. You may omit the creation of these backup files using the option __-B / --no-backup__.

Please note that &ldquo;masks&rdquo; is a special action set that disallows the application of some other actions so that, e.g., the dividers in ISBN numbers are not replaced by &amp;ndash;. The masks action set is given in [Appendix D](appendixD.md).

Examples
--------

```console
python degrotesque -i my_page.html -a quotes.german
```

Replaces single and double quotes within the file &ldquo;my_page.html&rdquo; by their typographic German counterparts.

```console
python degrotesque -i my_folder -r --no-backup
```

Applies the default actions to all files that match the extension in the folder &ldquo;my_folder&rdquo; and all subfolders. No backup files are generated.


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

