ChangeLog for degrotesque
=========================

to come: degrotesque-3.0.0
--------------------------

* Added support for processing plain text files; The distinction whether a file is a plain text file or a HTML/XML derivative is done using the extension (see Appendix B for used extensions) and by evaluating the contents; Everything is replaced in text files. When processing a file as a XML/HTML derivative, elements are skipped. Introducing the options __--text__ / __-T__ and __--html__ / __-H__ to explicitly set the file type.
* Supporting different target encodings for the replacements using the __--format / -f _&lt;FORMAT&gt;___ option (the option __--unicode__ / __-u__ was removed):
    * &#8216;__unicode__&#8217;: uses numeric entities (e.g. &#8216;&amp;#8211;&#8217; for an &#8216;&mdash;&#8217;);
    * &#8216;__html__&#8217;: uses numeric entities (e.g. &#8216;&amp;mdash;&#8217; for an &#8216;&mdash;&#8217;);
    * &#8216;__text__&#8217;: uses plain (utf-8) characters (e.g. &#8216;—&#8217; for an &#8216;&mdash;&#8217;).
* 100 % test coverage :-)


degrotesque-2.0.6 (05.02.2023)
------------------------------

* Patched documentation (return types)
* Set proper formatting for [readthedocs](https://degrotesque.readthedocs.io/en/2.0.6/)
* It&apos;s not 2.0.4 due to caching by readthedocs


degrotesque-2.0.2 (04.02.2023)
------------------------------

* Corrected installation and execution as a console script


degrotesque-2.0 (05.01.2023)
----------------------------

* Changed the license to [BSD](license.md).
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
* added a [HowToRelease](https://github.com/dkrajzew/degrotesque/blob/master/HowToRelease.md) file


degrotesque-1.2 (30.05.2020)
----------------------------
* [issue #8](https://github.com/dkrajzew/degrotesque/issues/8): added a [ChangeLog](https://github.com/dkrajzew/degrotesque/blob/master/CHANGES.md) file 
* [issue #6](https://github.com/dkrajzew/degrotesque/issues/6): using a lower-case version of HTML when skipping elements
* [issue #9](https://github.com/dkrajzew/degrotesque/issues/9): change LICENCE to LGPL
* [issue #7](https://github.com/dkrajzew/degrotesque/issues/7): add an API description
* Added a masking function for not replacing minusses in ISBN and ISSN


degrotesque-1.0 (13.05.2020)
----------------------------
First complete release



