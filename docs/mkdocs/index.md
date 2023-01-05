[![License: BSD](https://img.shields.io/badge/License-BSD-green.svg)](https://github.com/dkrajzew/degrotesque/blob/master/LICENSE)
[![PyPI version](https://badge.fury.io/py/degrotesque.svg)](https://pypi.python.org/pypi/degrotesque)
![test](https://github.com/dkrajzew/degrotesque/actions/workflows/test.yml/badge.svg)
[![Downloads](https://pepy.tech/badge/degrotesque)](https://pepy.tech/project/degrotesque)
[![Coverage](https://img.shields.io/badge/coverage-98%25-success)](https://img.shields.io/badge/coverage-98%25-success)


degrotesque &mdash; A web type setter.

Introduction
============

*degrotesque beautifies the web.*

**degrotesque** is a [Python](https://www.python.org/) script. It loads an HTML file from the disc — or several in batch, one after the other — and for each, it replaces some commonly used non-typographic characters, such as ", ', -, etc. into their typographic representant for improving the pages&apos; appearance.

E.g.:

 "Well - that's not what I had expected."

will become:

 &ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;

I think, it looks __much__ better.

The starting and ending quotes have been replaced by &ldquo; and &rdquo;, respectively, the ' by &apos; and the - by an &mdash;. Of course, this script omits HTML-elements. It keeps the complete format as-is, and replaces characters by their proper HTML entity name or the respective unicode character.

It is meant to be a relatively **reliable post-processing step for web pages before releasing them**.


Background
==========

I often write my texts and web pages using a plain editor. As such, the character " is always used for quotes, a dash is always a minus, etc.

I wanted to have a tool that automatically recognizes which characters should be replaced by their more typographic counterpart and applies the according rules.

I think it's a pity that major Desktop Publishing applications do this on the fly but many and even major web sites still show us plain ASCII characters.

**degrotesque** does the job pretty fine. After writing / building my pages, the tool converts them to a prettier and typographically more correct form. The structure and format of the pages is completely remained. And as said, it works reliable.

If you need any consultations, please let me know. If you know better, too.


License
=======

__degrotesque__ is licensed under the [BSD license](LICENSE).