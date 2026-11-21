# Implementation Notes

## Why masking?

I tried [Genshi](https://genshi.edgewall.org/), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/), and [lxml](https://lxml.de/). All missed in keeping the code unchanged. That's why marking was introduced. The HTML marker just skips HTML-elements and the contents of some special elements.

## Why no per-file-type replacement defaults?

I thought it would make sense to have defaults for the replacement format ('character', 'unicode', 'html') per file type.

No, in most cases, you want to have plain unicode characters to be inserted. This counts for text files, markdown files, restructuredText files, at least. It does not make sense to use something different for source file comments, either. As such, both, doxygen, and Python files would use plain unicode characters as well.

There is only the distinction between HTML and non-HTML SGML files. And here, the number of possible variants, workflows, and destinations is legion. As such, no, in this case, you have to define what is wanted.

## Why open source?

Because I like open source and have been quite successful doing it.


