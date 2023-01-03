Implementation Notes
====================

.. _notes:


- I tried `Genshi <https://genshi.edgewall.org/>`_, `BeautifulSoup <https://www.crummy.com/software/BeautifulSoup/>`_, and `lxml <https://lxml.de/>`_. All missed in keeping the code unchanged. So the parser just skips HTML-elements and the contents of some special elements, see above. Works in most cases.


