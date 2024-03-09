Running on the Command Line
===========================

__degrotesque__ is implemented in [Python](https://www.python.org/). It is started on the command line.


Description
-----------

The option __-i _&lt;PATH&gt;___ / __--input _&lt;PATH&gt;___ tells the script which file(s) shall be read &mdash; you may name a file or a folder, here. If the option __-r__ / __--recursive__ is set, the given folder will be processed recursively.

The tool processes text files, HTML files, XML files, and their derivatives. Per default, all files are processed when **-i**  points to a folder. You may limit the files to process by their extension using the __-e _&lt;EXTENSION&gt;[,&lt;EXTENSION&gt;]\*___ / __--extensions _&lt;EXTENSION&gt;[,&lt;EXTENSION&gt;]*___ option. The files are assumed to be encoded using UTF-8 per default. You may change the encoding using the option __-E _&lt;ENCODING&gt;___ / __--encoding _&lt;ENCODING&gt;___.

The files are read one by one and the replacement of plain ASCII chars by some nicer ones is based upon a chosen set of &ldquo;actions&rdquo;. Known and default actions are given in [Appendix A](appendixA.md). You may select the actions to apply using the __-a _&lt;ACTION_NAME&gt;[,&lt;ACTION_NAME&gt;]*___ / __--actions _&lt;ACTION_NAME&gt;[,&lt;ACTION_NAME&gt;]\*___ option. The default actions are &#8216;_masks_&#8217;, &#8216;_quotes.english_&#8217;, &#8216;_dashes_&#8217;, &#8216;_ellipsis_&#8217;, &#8216;_math_&#8217;, &#8216;_apostrophe_&#8217;, and &#8216;_commercial_&#8217;.

Per default, Unicode entities are inserted (e.g. &#8216;&amp;#8211;&#8217; for an &#8216;&mdash;&#8217;). You may change this using the __--format _&lt;FORMAT&gt;___ / __-f _&lt;FORMAT&gt;___. The following formats are currently supported:

* &#8216;__unicode__&#8217;: uses numeric entities (e.g. &#8216;&amp;#8211;&#8217; for an &#8216;&mdash;&#8217;);
* &#8216;__html__&#8217;: uses numeric entities (e.g. &#8216;&amp;mdash;&#8217; for an &#8216;&mdash;&#8217;);
* &#8216;__text__&#8217;: uses plain (utf-8) characters (e.g. &#8216;—&#8217; for an &#8216;&mdash;&#8217;).


__degrotesque__ tries to determine whether the read files are plain text files, markdown files, or XML or HTML derivatives using the files&amp; extensions and contents. [Appendix B](appendixB.md) lists the extensions by which files are recognized as HTML / markdown files. To be secure, one may set __--html__ / __-H__ when processing HTML files, __--markdown__ / __-M__ when processing markdown files, or __--text__ / __-T__ when processing plain text files.

When parsing XML/HTML files, the script does not change the quotation marks within elements, of course. As well, the contents of several elements, such as &lt;code&gt; or &lt;pre&gt;, are skipped. You may change the list of elements which contents shall not be processed using the option __-s _&lt;ELEMENT_NAME&gt;[,&lt;ELEMENT_NAME&gt;]*___ / __--skip _&lt;ELEMENT_NAME&gt;[,&lt;ELEMENT_NAME&gt;]\*___. The list of elements that are skipped per default is given in [Appendix C](appendixC.md).

When parsing markdown files, code &mdash; both indented and defined using ` &mdash; is skipped. Quotes as well.

After the actions have been applied to its contents, the file is saved. By default, a backup of the original file is saved under the same name, with the appendix &ldquo;.orig&rdquo;. You may omit the creation of these backup files using the option __-B / --no-backup__.

The option __--help__ / __-h__ prints a help screen. The option __--version__ the __degrotesque&apos;s__ version number.

Please note that &ldquo;masks&rdquo; is a special action set that disallows the application of some other actions so that, e.g., the dividers in ISBN numbers are not replaced by &amp;ndash;. The masks action set is given in [Appendix D](appendixD.md).

Examples
--------

```console
degrotesque --input my_page.html --actions quotes.german
```

Replaces single and double quotes within the file &ldquo;my_page.html&rdquo; by their typographic German counterparts.

```console
degrotesque --input my_folder --recursive --no-backup
```

Applies the default actions to all files in the folder &ldquo;my_folder&rdquo; and all subfolders. No backup files are generated. The files format of each file is determined using the file&apos;s extension.


Command line arguments
----------------------

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

