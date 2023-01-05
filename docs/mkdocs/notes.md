Implementation Notes
====================

- I tried [Genshi](https://genshi.edgewall.org/), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/), and [lxml](https://lxml.de/). All missed in keeping the code unchanged. So the parser just skips HTML-elements and the contents of some special elements. Works in most cases.


