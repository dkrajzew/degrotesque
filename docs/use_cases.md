# Use Cases

## Improving web pages

I usually write my web pages uing a plain text editor.
As such, I do not use any nice punctuation.
Instead, I run degrotesque on the pages before putting them online.
The basic call is like

```shell
python degrotesque.py --input <PATH_TO_PAGES> --recursive -H
```

This tells degrotesque to process all files in the folder *&lt;PATH_TO_PAGES&gt;*
(**--input *&lt;PATH_TO_PAGES&gt;***) and all of its sub-folders (**--recursive**).
The -H switch tells degrotesque that the files are HTML/XML.


## Type setting for docbook documents

DocBook documents are defined using XML and can as such be processed by **degrotesque**.

The following call reads a DocBook document named "userdocs.xml", applies the actions,
and writes the result without generating a backup. As DocBook does not know HTML entities
(the HTML names for unicode characters) and hicks up when getting UTF-8 chars sometimes,
we set the option **-f unicode**. This will insert unicode character numbers.

```shell
python degrotesque.py --input userdocs.xml -B -f unicode
```


## Type setting for Markdown documentation

The pages with **degrotesque** documentation you currently look at were written 
using Markdown (mkdocs). To make them pretty, **degrotesque** was applied to the 
source md-files.

The call is:

```shell
python degrotesque.py --input docs/* -B
```


## Making source code pretty

Applying **degrotesque** to source code may be interesting when using, e.g.
doxygen or mkdocs for generating a documentation.

```shell
python degrotesque.py --input <PATH_TO_SOURCE_CODE> --recursive -!!!
```

This tells degrotesque to process all files in the folder *&lt;PATH_TO_SOURCE_CODE&gt;*
(**--input *&lt;PATH_TO_SOURCE_CODE&gt;***) and all of its sub-folders (**--recursive**).
The -!!! switch tells degrotesque that the files are HTML/XML.

Please note that in my opinion, there is some magic in having a plain ASCII source code.
Think whether you really want to have it type-setted.

