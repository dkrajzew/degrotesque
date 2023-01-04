degrotesque - A web type setter
===============================

.. contents

Introduction
------------

*degrotesque beautifies the web.*

The `Python <https://www.python.org/>`_ script **degrotesque** loads an HTML file from the disc — or several in batch, one after the other — and for each, it replaces some commonly used non-typographic characters, such as \", \', \-, etc. into their typographic representant for improving the pages' appearance.

E.g.:

\"Well - that\'s not what I had expected.\"

will become:

“Well — that's not what I had expected.”

I think, it looks **much** better.

The starting and ending quotes have been replaced by &ldquo; and &rdquo;, respectively, the \' by &apos; and the - by an &mdash;. Of course, this script omits HTML-elements. It keeps the complete format as-is, and replaces characters by their proper HTML entity name or the respective unicode character. 

It is meant to be a relatively **reliable post-processing step for web pages before releasing them**.


Background
----------

I often write my texts and web pages using a plain editor. As such, the character \" is always used for quotes, a dash is always a minus, etc.

I wanted to have a tool that automatically recognizes which characters should be replaced by their more typographic counterpart and applies the according rules. 

I think it's a pity that major Desktop Publishing applications do this on the fly but many and even major web sites still show us plain ASCII characters.

**degrotesque** does the job pretty fine. After writing / building my pages, the tool converts them to a prettier and typographically more correct form. The structure and format of the pages is completely remained. And as said, it works reliable.

If you need any consultations, let me know. If you know better, too.


Examples / Users
----------------

- `My own pages <https://www.krajzewicz.de/>`_;
- `PaletteWB <https://www.palettewb.com/>`_ — a sophisticated palette editor for MS Windows.


License
-------

**degrotesque** is licensed under the `BSD license <https://github.com/dkrajzew/degrotesque/blob/master/LICENSE>`_.


Contents
--------

.. toctree::
   :maxdepth: 2

   index
   usage
   changes
   api
   links
   appendices
   notes
   legal
