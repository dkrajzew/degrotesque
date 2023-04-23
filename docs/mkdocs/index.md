[![License: BSD](https://img.shields.io/badge/License-BSD-green.svg)](https://github.com/dkrajzew/degrotesque/blob/master/LICENSE)
[![PyPI version](https://badge.fury.io/py/degrotesque.svg)](https://pypi.python.org/pypi/degrotesque)
![test](https://github.com/dkrajzew/degrotesque/actions/workflows/test.yml/badge.svg)
[![Downloads](https://pepy.tech/badge/degrotesque)](https://pepy.tech/project/degrotesque)
[![Coverage](https://img.shields.io/badge/coverage-100%25-success)](https://img.shields.io/badge/coverage-100%25-success)
[![Documentation Status](https://readthedocs.org/projects/degrotesque/badge/?version=latest)](https://degrotesque.readthedocs.io/en/latest/?badge=latest)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=GVQQWZKB6FDES)


degrotesque &mdash; A web type setter.

Introduction
------------

*degrotesque beautifies the web.*

**degrotesque** is a [Python](https://www.python.org/) script. It loads a text/markdown/HTML/XML file from the disc &mdash; or several in batch &mdash; and for each, it replaces some commonly used non-typographic characters, such as ", ', -, etc. into their typographic representation for improving the pages&apos; appearance.

E.g.:

 "Well - that's not what I had expected."

will become:

 &ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;

I think it looks __much__ better.

The starting and ending quotes have been replaced by &ldquo; and &rdquo;, respectively, the ' by &apos; and the - by an &mdash;. Of course, this script omits HTML-elements. It keeps the complete format as-is, and replaces characters by their proper HTML entity name or the respective unicode character.

It is meant to be a relatively **reliable post-processing step for type setting web pages before releasing them**. Being a Python script, **it can be easily embedded in own workflows**. In version 3.0.0 the support of markdown files was added.

**degrotesque** supports English, German, and French alternatives currently.


Examples
--------

```console
degrotesque -i my_page.html -a quotes.german
```

Replaces single and double quotes within the file &ldquo;my_page.html&rdquo; by their typographic German counterparts.

```console
degrotesque -i my_folder -r --no-backup
```

Applies the default actions to all files in the folder &ldquo;my_folder&rdquo; and all subfolders. No backup files are generated. The files format of each file is determined using the file&apos;s extension.


Background
----------

I often write my texts and web pages using a plain editor. As such, the character " is always used for quotes, a dash is always a minus, etc.

I wanted to have a tool that automatically recognizes which characters should be replaced by their more typographic counterpart and applies the according rules.

I think it&rsquo;s a pity that major Desktop Publishing applications do this on the fly but many and even major web sites still show us plain ASCII characters.

**degrotesque** does the job pretty fine. After writing / building my pages, the tool converts them to a prettier and typographically more correct form. The structure and format of the pages is completely remained. And as said, it works reliable.

If you need any consultations, please let me know. If you know better, too.


Future Plans
------------

As **degrotesque** can meanwhile parse not only HTML and plain text files, but as well Markdown files, the next step would be to open it to other file formats as well. As well, other languages besides English, German, and French could be covered.

* Add support for further file and mark types.
* Add support for further languages.

We would love to extend **degrotesque** to cover these use cases, but only if someone is interested :-) You may drop us a mail at daniel@krajzewicz.de.


License
-------

__degrotesque__ is licensed under the [BSD license](license.md).
