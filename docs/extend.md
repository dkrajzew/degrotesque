Extending degrotesque
=====================

Adding a new file format
------------------------

Adding a new file format is mainly done by implementing a new computation of
the mask that says which parts shall be processed and which not (see [Workflow](workflow.md)).

To improve the extensibility of degrotesque, the methods that compute the masks
in dependence to the file type have been extracted from the Degrotesque class
and are now subclasses of the class "DegrotesqueMarker", defined in marker.py. 

Two methods must be implemented:

* __get_extensions__: Returns a list of file extensions that shall be processed by
this marker
* __get_mask__: gets the document's file name and contents and must return the mask.


As such, to extend degrotesque by a new file format the following steps are
to be done:

* build a subclass of DegrotesqueMarker and store it in a file named "marker_*&lt;YOUR_FORMAT&gt;.py*"
* define the file extensions this marker is responsible for in the classes' **get_extensions** method
* implement the mask computation in the class' **get_mask** method; the mask must have the same length as the original text and should be made of the characters '0' (which will be processed) and '1' (which will be skipped)
* add your marker class to degrotesque's \_\_init\_\_ method

# Closing notes

If you have extended **degrotesque**, please let me know. I am accepting code from 
third parties and people may need what you have done.

