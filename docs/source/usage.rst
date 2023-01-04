Usage
=====

.. _installation:



Download and Installation
-------------------------

The **current version** is `degrotesque-1.6 <https://github.com/dkrajzew/degrotesque/releases/tag/1.6>`_. You may **install degrotesque** using

``python -m pip install degrotesque``

You may **download a copy or fork the code** at `degrotesque's github page <https://github.com/dkrajzew/degrotesque>`_. Besides, you may **download the current release** here:

- `degrotesque-1.6.zip <https://github.com/dkrajzew/degrotesque/archive/refs/tags/1.6.zip>`_
- `degrotesque-1.6.tar.gz <https://github.com/dkrajzew/degrotesque/archive/refs/tags/1.6.tar.gz>`_


Using as a standalone script
----------------------------

**degrotesque** is implemented in `Python <https://www.python.org/>`_. It is started on the command line.

The option **-i <PATH>** / **\-\-input <PATH>** tells the script which file(s) shall be read - you may name a file or a folder, here. If the option **-r** / **\-\-recursive** is set, the given folder will be processed recursively.

The tool processes HTML files, XML files, and their derivatives. The extensions of file types that are processed are given in :ref:`appendix-a`. You may change the extensions of files to process using the **-e <EXTENSION>[,<EXTENSION>]\*** / **\-\-extensions <EXTENSION>[,<EXTENSION>]\*** option.

The files are read one by one and the replacement of plain ASCII chars by some nicer ones is based upon a chosen set of "actions". Known and default actions are given in :ref:`appendix-b`. You may select the actions to apply using the **-a <ACTION_NAME>[,<ACTION_NAME>]\*** / **\-\-actions <ACTION_NAME>[,<ACTION_NAME>]\*** option. The default actions are **masks**, **quotes.english**, **dashes**, **ellipsis**, **math**, and **apostrophe**. Per default, HTML entities are inserted. If you rather wish to have unicode values, use the option **-u** / **\-\-unicode**.

The files are assumed to be encoded using UTF-8 per default. You may change the encoding using the option **-E <ENCODING>** / **\-\-encoding <ENCODING>**.

The script does not change the quotation marks of HTML elements, of course. As well, the contents of several elements, such as <code> or <pre>, are skipped. You may change the list of elements which contents shall not be processed using the option **-s <ELEMENT_NAME>[,<ELEMENT_NAME>]\*** / **\-\-skip <ELEMENT_NAME>[,<ELEMENT_NAME>]\***. The list of elements that are skipped per default is given in :ref:`appendix-c`.

After the actions have been applied to its contents, the file is saved. By default, a backup of the original file is saved under the same name, with the appendix ".orig". You may omit the creation of these backup files using the option **-B / \-\-no-backup**.

Please note that "masks" is a special action set that disallows the application of some other actions so that, e.g., the dividers in ISBN numbers are not replaced by &ndash;. The masks action set is given in :ref:`appendix-d`.

Options
^^^^^^^

The script has the following options:

- **\-\-input/-i <PATH>**: the file or the folder to process
- **\-\-recursive/-r**: Set if the folder &mdash; if given &mdash; shall be processed recursively
- **\-\-no-backup/-B**: Set if no backup files shall be generated
- **\-\-unicode/-u**: When set, unicode characters instead of HTML-entities are used
- **\-\-extensions/-e <EXTENSION>[,<EXTENSION>]\***: The extensions of files that shall be processed
- **\-\-encoding/-E <ENCODING>**: The assumed encoding of the files
- **\-\-skip/-s <ELEMENT_NAME>[,<ELEMENT_NAME>]\***: Elements which contents shall not be changed
- **\-\-actions/-a <ACTION_NAME>[,<ACTION_NAME>]\***: Name the actions that shall be applied
- **\-\-help**: Prints the help screen


Examples
^^^^^^^^

``degrotesque -i my_page.html -a quotes.german``

Replaces single and double quotes within the file "my_page.html" by their typographic German counterparts.

``degrotesque -i my_folder -r --no-backup``

Applies the default actions to all files that match the extension in the folder "my_folder" and all subfolders. No backup files are generated.


Embedding in own applications (API)
-----------------------------------

You may as well embed **degrotesque** within your own applications. The usage is very straightforward::

   import degrotesque
   # build the degrotesque instance with default values
   degrotesque = degrotesque.Degrotesque()
   # apply degroteque
   prettyTextHTML = degrotesque.prettify(plainHTML)


The default values can be replaced using some of the class' interfaces (methods)::

   # change the actions to apply (by naming them)
   # here: apply french quotes and math symbols
   degrotesque.setActions("quotes.french,math")
   # change the elements which contents shall be skipped
   # here: skip the contents of "code", 
   #  "script", and "style" elements
   degrotesque.setToSkip("code,script,style")



