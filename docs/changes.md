# ChangeLog for degrotesque

## degrotesque-4.0.0 (to come)

* Integrations
	* [Coveralls](https://coveralls.io/) integration ([![Coverage Status](https://coveralls.io/repos/github/dkrajzew/degrotesque/badge.svg?branch=main)](https://coveralls.io/github/dkrajzew/degrotesque?branch=main))
	* [readthedocs](https://readthedocs.io/) integration ([![Documentation Status](https://readthedocs.org/projects/degrotesque/badge/?version=latest)](https://degrotesque.readthedocs.io/en/latest/?badge=latest))
* Extensions
	* Added processing of comments in Python files
	* Added processing of comments in [doxygen](https://www.doxygen.nl/) documentation (\*.cpp, \*.h, \*.java)
	* Added processing of Markdown files
	* Added processing of restructuredText files
	* Added actions for arrows (see [Appendix A](appendixA.md))
	* Added support for configuration files
* Refactoring
	* File type dependent functions for determining which parts of the respective document shall be processed were extracted into own sub-files
	* Moved helper methods to an own file
	* Proper variable and function / methods names
	* Added type hints
	* Added a direct method to prettify / degrotesque a document
	* Replaced OptionsParser by argparse
	* Improved XML/HTML-file recognition from contents
	* Using a single command line option for forcing a file type
* Documentation
	* Proper Python documentation
* Deployment
	* Different requirement files for different purposes

## degrotesque-3.0.0 (26.03.2023)

* Adding support for degrotesquing markdown files (contents of code and quotes are kept)
* Added support for processing plain text files; The distinction whether a file is a plain text file or a HTML/XML derivative is done using the extension (see Appendix B for used extensions) and by evaluating the contents; Everything is replaced in text files. When processing a file as a XML/HTML derivative, elements are skipped. Introducing the options __--text__ / __-T__, __--markdown__ / __-M__, and __--html__ / __-H__ to explicitly set the file type.
* Supporting different target encodings for the replacements using the __--format / -f _&lt;FORMAT&gt;___ option (the option __--unicode__ / __-u__ was removed):
    * &#8216;__unicode__&#8217;: uses numeric entities (e.g. &#8216;&amp;#8211;&#8217; for an &#8216;&mdash;&#8217;);
    * &#8216;__html__&#8217;: uses numeric entities (e.g. &#8216;&amp;mdash;&#8217; for an &#8216;&mdash;&#8217;);
    * &#8216;__text__&#8217;: uses plain (utf-8) characters (e.g. &#8216;—&#8217; for an &#8216;&mdash;&#8217;).
* 100% test coverage :-)
* renamed master branch to main


## degrotesque-2.0.6 (05.02.2023)

* Patched documentation (return types)
* Set proper formatting for [readthedocs](https://degrotesque.readthedocs.io/en/2.0.6/)
* It&apos;s not 2.0.4 due to caching by readthedocs


## degrotesque-2.0.2 (04.02.2023)

* Corrected installation and execution as a console script


## degrotesque-2.0 (05.01.2023)

* Changed the license to [BSD](license.md).
* Using github actions for testing on push instead of using Travis CI
* Cleaned up project tree
* Adding an [mkdocs](https://www.mkdocs.org/) documentation


## degrotesque-1.6 (16.07.2022)

* reworked tests, now using pytest and unittest
* [issue #10](https://github.com/dkrajzew/degrotesque/issues/10): will not use TextTest here; using pytest instead
* [issue #11](https://github.com/dkrajzew/degrotesque/issues/11): using coverage.py instead of coveralls
* added the -u/--unicode option which forces to use unicode codes instead of HTML entities


## degrotesque-1.4 (19.07.2021)

* debugged the parser &mdash; could not parse code-in-code tags (weird it&apos;s even allowed, xsltproc generates this)
* added a [HowToRelease](https://github.com/dkrajzew/degrotesque/blob/master/HowToRelease.md) file


## degrotesque-1.2 (30.05.2020)

* [issue #8](https://github.com/dkrajzew/degrotesque/issues/8): added a [ChangeLog](https://github.com/dkrajzew/degrotesque/blob/master/CHANGES.md) file
* [issue #6](https://github.com/dkrajzew/degrotesque/issues/6): using a lower-case version of HTML when skipping elements
* [issue #9](https://github.com/dkrajzew/degrotesque/issues/9): change LICENCE to LGPL
* [issue #7](https://github.com/dkrajzew/degrotesque/issues/7): add an API description
* Added a masking function for not replacing minusses in ISBN and ISSN


## degrotesque-1.0 (13.05.2020)

First complete release



