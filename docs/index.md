[![License: BSD](https://img.shields.io/badge/License-BSD-green.svg)](https://github.com/dkrajzew/degrotesque/blob/master/LICENSE)
[![PyPI version](https://badge.fury.io/py/degrotesque.svg)](https://pypi.python.org/pypi/degrotesque)
![test](https://github.com/dkrajzew/degrotesque/actions/workflows/test.yml/badge.svg)
[![Downloads](https://pepy.tech/badge/degrotesque)](https://pepy.tech/project/degrotesque)
[![Downloads](https://static.pepy.tech/badge/degrotesque/week)](https://pepy.tech/project/degrotesque)
[![Coverage Status](https://coveralls.io/repos/github/dkrajzew/degrotesque/badge.svg?branch=main)](https://coveralls.io/github/dkrajzew/degrotesque?branch=main)
[![Dependecies](https://img.shields.io/badge/dependencies-none-green)](https://img.shields.io/badge/dependencies-none-green)
[![Documentation Status](https://readthedocs.org/projects/degrotesque/badge/?version=latest)](https://degrotesque.readthedocs.io/en/latest/?badge=latest)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=GVQQWZKB6FDES)


degrotesque &mdash; A web type setter written in Python.

Introduction
------------

*degrotesque beautifies the web.*

**degrotesque** is a command line script written in the [Python](https://www.python.org/) programming language 
that loads a text/markdown/HTML/XML/Python/Java/... file from the disc &mdash; or several in batch &mdash; and for each, it 
replaces some commonly used non-typographic characters like hyphens, single and double quotes, etc. into their typographic 
representation for improving the text&apos;s appearance. Of course, non-text parts of the respective document, like e.g. 
HTML-tags, code, or what, are omitted.

E.g.:

<center><h1 class="degrotesque_example">"Well - that's not what I had expected."</h1></center>

will become:

<center><h1 class="degrotesque_example">&ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;</h1></center>

I think it looks __much__ better.

The starting and ending quotes have been replaced by &ldquo; and &rdquo;, respectively.
The ' has been replaced by &apos; and the - by an &mdash;.
Of course, this script omits HTML elements. It keeps the complete format as-is, and replaces characters by their proper HTML entity name or the respective unicode character.

**degrotesque** is meant to be a relatively **reliable post-processing step for type setting web pages or any plain texts before releasing them**.
Being a [Python](https://www.python.org/) script, **it can be easily embedded in own workflows** and can be used on almost all operating systems.

**degrotesque** supports English, German, and French alternatives currently.


Examples
--------

```console
degrotesque --input my_page.html --actions quotes.german
```

Replaces single and double quotes within the file &ldquo;my_page.html&rdquo; by their typographic German counterparts.

```console
degrotesque --input my_folder --recursive --no-backup
```

Applies the default actions to all files in the folder &ldquo;my_folder&rdquo; and all subfolders. No backup files are generated. The format of each file is determined using the respective file&apos;s extension.


Background
----------

I often write my texts, documentation and web pages using a plain editor. As such, the character " is always used for quotes, a dash is always a minus, etc.

I wanted to have a tool that automatically recognizes which characters should be replaced by their more typographic counterpart and applies the according rules.

I think it&apos;s a pity that major Desktop Publishing applications do this on the fly but many and even major web sites still show us plain ASCII characters.

**degrotesque** does the job pretty fine. After writing / building my pages, the tool converts them to a prettier and typographically more correct form. The structure and format of the pages is completely remained. And as said, **degrotesque** works reliable.

If you need any consultations, please let me know. If you know better, too.


Future Plans
------------

**degrotesque** is working for me as intended.
With the current release, all features I had in mind were implemented.
As such, I suppose that new versions of **degrotesque** will only be released if someone puts new features on the table. If you need something, you may drop me a mail at daniel@krajzewicz.de.


License
-------

__degrotesque__ is licensed under the [BSD license](license.md).
