ChangeLog
=========

degrotesque-1.6 (16.07.2022)
----------------------------

- reworked tests, now using pytest and unittest
- `[issue #10] <https://github.com/dkrajzew/degrotesque/issues/10>`_: will not use TextTest here; using pytest instead 
- `[issue #11] <https://github.com/dkrajzew/degrotesque/issues/11>`_: using coverage.py instead of coveralls
- added the -u/--unicode option which forces to use unicode codes instead of HTML entities


degrotesque-1.4 (19.07.2021)
----------------------------

- debugged the parser - could not parse code-in-code tags (weird it's even allowed, xsltproc generates this)
- added a `HowToRelease <https://github.com/dkrajzew/degrotesque/blob/master/HowToRelease.md>`_ file


degrotesque-1.2 (30.05.2020)
----------------------------

- `[issue #8] <https://github.com/dkrajzew/degrotesque/issues/8>`_: added a `HowToRelease <https://github.com/dkrajzew/degrotesque/blob/master/CHANGES.md>`_ file
- `[issue #6] <https://github.com/dkrajzew/degrotesque/issues/6>`_: using a lower-case version of HTML when skipping elements
- `[issue #9] <https://github.com/dkrajzew/degrotesque/issues/9>`_: change LICENCE to LGPL
- `[issue #7] <https://github.com/dkrajzew/degrotesque/issues/7>`_: add an API description
- Added a masking function for not replacing minusses in ISBN and ISSN


degrotesque-1.0 (13.05.2020)
----------------------------
First complete release



