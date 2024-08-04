Release Steps
=============

* check the [ChangeLog](https://github.com/dkrajzew/degrotesque/blob/master/docs/mkdocs/changes.md)
* patch the release number and the copyright information in
    * the [README.md](https://github.com/dkrajzew/degrotesque/blob/master/README.md) file
    * the [setup.py](https://github.com/dkrajzew/degrotesque/blob/master/setup.py) file
    * all python files
    * the [install.md](https://github.com/dkrajzew/degrotesque/blob/master/docs/install.md) file
* run the tests (run tests/run_tests.bat)
* build the pydoc documentation, copy it to the web pages
* commit changes
* build the github release (tag: ___&lt;VERSION&gt;___, name: __degrotesque-_&lt;VERSION&gt;___)
* build the PyPI release (see docs/build_release.bat)
