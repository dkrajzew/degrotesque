Extending degrotesque
=====================

Adding a new file format
------------------------

When processing plain text files, degrotesque is applied to the whole content.
This cannot be done when processing XML, HTML, or Markdown files as some 
parts - elements, attributes in XML/HTML-files or code parts in Markdown 
files - must be omitted.

This is the major thing to regard when extending degrotesque by new file types.

Internally, after loading a file, degrotesque computes a mask. The mask shows
which parts of the file contents shall be processed and which ones shall be
omitted. 

The mask is a string of the same length as the file contents. Parts that shall be 
processed are represented by a '0' ("zero" character), parts to omit by a '1' 
("one" character). degrotesque simply skips the parts marked with a '1'.

To improve the extensibility of degrotesque, the methods that compute the masks
for XML/HTML and Markdown files have been extracted from the Degrotesque class
and are now subclasses of the class "DegrotesqueMarker", defined in marker.py. 

Two methods must be implemented:

* __get_extensions__: Returns a list of file extensions that shall be processed by
this marker
* __get_mask__: gets the document's file name and contents and must return the mask.


As such, to extend degrotesque by a new file format the following steps are
to be done:

* build a subclass of DegrotesqueMarker and store it in a file named "marker_*&lt;YOUR_FORMAT&gt;*"
* define the files extensions to use in the classes' **get_extensions** method
* implement the mask computation in the class' **get_mask** method; the mask must have the same length as the original text and should be made of the characters '0' (which will be processed) and '1' (which will be skipped)
* add your marker class to degrotesque's \_\_init\_\_ method


