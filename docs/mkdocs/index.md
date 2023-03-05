[![License: BSD](https://img.shields.io/badge/License-BSD-green.svg)](https://github.com/dkrajzew/degrotesque/blob/master/LICENSE)
[![PyPI version](https://badge.fury.io/py/degrotesque.svg)](https://pypi.python.org/pypi/degrotesque)
![test](https://github.com/dkrajzew/degrotesque/actions/workflows/test.yml/badge.svg)
[![Downloads](https://pepy.tech/badge/degrotesque)](https://pepy.tech/project/degrotesque)
[![Coverage](https://img.shields.io/badge/coverage-100%25-success)](https://img.shields.io/badge/coverage-100%25-success)
[![Documentation Status](https://readthedocs.org/projects/degrotesque/badge/?version=latest)](https://degrotesque.readthedocs.io/en/latest/?badge=latest)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=GVQQWZKB6FDES)



degrotesque &mdash; A web type setter.

Introduction
============

*degrotesque beautifies the web.*

**degrotesque** is a [Python](https://www.python.org/) script. It loads a text/HTML/XML file from the disc — or several in batch, one after the other — and for each, it replaces some commonly used non-typographic characters, such as ", ', -, etc. into their typographic representation for improving the pages&apos; appearance.

E.g.:

 "Well - that's not what I had expected."

will become:

 &ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;

I think it looks __much__ better.

The starting and ending quotes have been replaced by &ldquo; and &rdquo;, respectively, the ' by &apos; and the - by an &mdash;. Of course, this script omits HTML-elements. It keeps the complete format as-is, and replaces characters by their proper HTML entity name or the respective unicode character.

It is meant to be a relatively **reliable post-processing step for web pages before releasing them**.


Examples
--------

```console
degrotesque -i my_page.html -a quotes.german
```

Replaces single and double quotes within the file &ldquo;my_page.html&rdquo; by their typographic German counterparts.

```console
degrotesque -i my_folder -r --no-backup
```

Applies the default actions to all files in the folder &ldquo;my_folder&rdquo; and all subfolders. No backup files are generated.


Background
----------

I often write my texts and web pages using a plain editor. As such, the character " is always used for quotes, a dash is always a minus, etc.

I wanted to have a tool that automatically recognizes which characters should be replaced by their more typographic counterpart and applies the according rules.

I think it&rsquo;s a pity that major Desktop Publishing applications do this on the fly but many and even major web sites still show us plain ASCII characters.

**degrotesque** does the job pretty fine. After writing / building my pages, the tool converts them to a prettier and typographically more correct form. The structure and format of the pages is completely remained. And as said, it works reliable.

If you need any consultations, please let me know. If you know better, too.


License
=======

__degrotesque__ is licensed under the [BSD license](license.md).
