# Running on the Command Line

__degrotesque__ is started on the command line.


## Synopsis

```shell
degrotesque [-h] [-c FILE] [--version] [-r] 
            [-e EXTENSIONS] [-E ENCODING]
            [-t {sgml,text,md,doxygen,python,rst}] 
			[-B] [-f {html,unicode,char}] [-s SKIP] 
			[-a ACTIONS] [-w FILE]
            input
```

## Description

__degrotesque__ reads one or multiple files named on the command line. Multiple files are read if the given name contains an asteriks (__'\*'__) or is a folder. If the option __-r__ / __--recursive__ is set and a folder is given, it will be processed recursively.

Per default, all files are processed when the given path  points to a folder. You may limit the files to process by their extension using the __-e _&lt;EXTENSION&gt;[,&lt;EXTENSION&gt;]\*___ / __--extensions _&lt;EXTENSION&gt;[,&lt;EXTENSION&gt;]*___ option - multiple file extensions can be given, separated using a ','.

The files are assumed to be encoded using UTF-8 per default. You may change the encoding using the option __-E _&lt;ENCODING&gt;___ / __--encoding _&lt;ENCODING&gt;___.

The files are read one by one and the replacement of plain characters by some nicer ones is based upon a chosen set of &ldquo;actions&rdquo;. Known actions are given in [Appendix A](appendixA.md). You may select the actions to apply using the __-a _&lt;ACTION_NAME&gt;[,&lt;ACTION_NAME&gt;]*___ / __--actions _&lt;ACTION_NAME&gt;[,&lt;ACTION_NAME&gt;]\*___ option. The default actions are &#8216;_quotes.english_&#8217;, &#8216;_dashes_&#8217;, &#8216;_ellipsis_&#8217;, &#8216;_math_&#8217;, &#8216;_apostrophe_&#8217;, and &#8216;_commercial_&#8217;.

Per default, Unicode characters are inserted (e.g. &#8216;—&#8217; for an mdash). You may change this using the __--format _&lt;FORMAT&gt;___ / __-f _&lt;FORMAT&gt;___ option. The following formats are currently supported:

* &#8216;__unicode__&#8217;: uses numeric entities (e.g. &#8216;&amp;#8211;&#8217; for an &#8216;&mdash;&#8217;);
* &#8216;__html__&#8217;: uses HTML entities (e.g. &#8216;&amp;mdash;&#8217; for an &#8216;&mdash;&#8217;);
* &#8216;__char__&#8217;: uses plain (utf-8) characters (e.g. &#8216;—&#8217; for an &#8216;&mdash;&#8217;).


**degrotesque** tries to determine whether the read files are plain text files, markdown files, or XML/HTML derivatives using the files&apos; extensions and contents. [Appendix B](appendixB.md) lists the extensions by which files are recognized as HTML / markdown files. To be secure, one may set the file type using the __-t _&lt;TYPE&gt;___ / __--type _&lt;TYPE&gt;___ option. The following types are currently recognized:

* &#8216;__sgml__&#8217;: used for processing XML/HTML documents;
* &#8216;__text__&#8217;: used for processing plain text files;
* &#8216;__md__&#8217;: used for processing Markdown documents;
* &#8216;__doxygen__&#8217;: used for processing files documents using the Doxygen syntax;
* &#8216;__python__&#8217;: used for processing Python files;
* &#8216;__rst__&#8217;: used for processing restructuredText documents.

When parsing XML/HTML files, the script does not change the quotation marks within elements, of course. As well, the contents of several elements, such as &lt;code&gt; or &lt;pre&gt;, are skipped. You may change the list of elements which contents shall not be processed using the option __-s _&lt;ELEMENT_NAME&gt;[,&lt;ELEMENT_NAME&gt;]*___ / __--skip _&lt;ELEMENT_NAME&gt;[,&lt;ELEMENT_NAME&gt;]\*___. The list of elements that are skipped per default is given in [Appendix C](appendixC.md). This works only if the set / determined file type is &#8216;__sgml__&#8217;.

When parsing Markdown and restructuredText files, code is skipped. Quotes as well. When parsing doxygen files, only the contents of the doxygen-comments are processed. Only comments are processed in Python files, skipping pydoctest parts. The complete content of text files is processed. URLs and ISBN/ISSN numbers are always skipped (as well in text files), see [Appendix D](appendixD.md).

After the actions have been applied to its contents, the file is saved. By default, a backup of the original file is saved under the same name, with the appendix &ldquo;.orig&rdquo;. You may omit the creation of these backup files using the option __-B / --no-backup__.

You may as well define all the options in a configuration file. The options set within the configuration file must be preceeded by a line with "[degrotesque]". You can define the configuration file to load using the option __-c _&lt;FILE&gt;___ / __--config _&lt;FILE&gt;___. You may generate a configuration file that contains the currently given options using the option __-w _&lt;FILE&gt;___ / __--write-config _&lt;FILE&gt;___

The option __--help__ / __-h__ prints a help screen. The option __--version__ the __degrotesque&apos;s__ version number.

## Examples

```console
degrotesque --actions quotes.german my_page.html
```

Replaces single and double quotes within the file &ldquo;my_page.html&rdquo; by their typographic German counterparts.

```console
degrotesque --recursive --no-backup my_folder
```

Applies the default actions to all files in the folder &ldquo;my_folder&rdquo; and all subfolders. No backup files are generated. The files format of each file is determined using the file&apos;s extension.


## Command line arguments

The script can be started on the command line with the following options:

* __--config/-c _&lt;FILE&gt;___: Load options from the named cofniguration file
* __--recursive/-r__: Set if the folder &mdash; if given &mdash; shall be processed recursively
* __--extensions/-e _&lt;EXTENSION&gt;[,&lt;EXTENSION&gt;]*___: The extensions of files that shall be processed
* __--encoding/-E _&lt;ENCODING&gt;___: The assumed encoding of the files
* __--type/-t__: Defines the file type of the read files
* __--no-backup/-B__: Set if no backup files shall be generated
* __--format/-f _&lt;FORMAT&gt;___: Define the format of the replacements [&#8216;_html_&#8217;, &#8216;_unicode_&#8217;, &#8216;_char_&#8217;]
* __--skip/-s _&lt;ELEMENT_NAME&gt;[,&lt;ELEMENT_NAME&gt;]*___: Elements which contents shall not be changed
* __--actions/-a _&lt;ACTION_NAME&gt;[,&lt;ACTION_NAME&gt;]*___: Name the actions that shall be applied
* __--write-config/-w _&lt;FILE&gt;___: Save the current options into the named file (generate a configuration file)
* __--help__: Prints the help screen
* __--version__: Prints the version

