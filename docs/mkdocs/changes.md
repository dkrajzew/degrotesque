ChangeLog for degrotesque
=========================

degrotesque-2.0 (05.01.2023)
----------------------------

* Changed the license to [BSD](https://github.com/dkrajzew/degrotesque/LICENSE).
* Using github actions for testing on push instead of using Travis CI
* Cleaned up project tree
* Adding an [mkdocs](https://www.mkdocs.org/) documentation


degrotesque-1.6 (16.07.2022)
----------------------------
* reworked tests, now using pytest and unittest
* [issue #10](https://github.com/dkrajzew/degrotesque/issues/10): will not use TextTest here; using pytest instead
* [issue #11](https://github.com/dkrajzew/degrotesque/issues/11): using coverage.py instead of coveralls
* added the -u/--unicode option which forces to use unicode codes instead of HTML entities


degrotesque-1.4 (19.07.2021)
----------------------------
* debugged the parser &mdash; could not parse code-in-code tags (weird it&apos;s even allowed, xsltproc generates this)
* added a HowToRelease file (https://github.com/dkrajzew/degrotesque/blob/master/HowToRelease.md)


degrotesque-1.2 (30.05.2020)
----------------------------
* [issue #8](https://github.com/dkrajzew/degrotesque/issues/8): added a ChangeLog file (https://github.com/dkrajzew/degrotesque/blob/master/CHANGES.md)
* [issue #6](https://github.com/dkrajzew/degrotesque/issues/6): using a lower-case version of HTML when skipping elements
* [issue #9](https://github.com/dkrajzew/degrotesque/issues/9): change LICENCE to LGPL
* [issue #7](https://github.com/dkrajzew/degrotesque/issues/7): add an API description
* Added a masking function for not replacing minusses in ISBN and ISSN


degrotesque-1.0 (13.05.2020)
----------------------------
First complete release



