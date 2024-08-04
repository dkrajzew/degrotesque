#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ===========================================================================
"""degrotesque - A masking class with begin / end strings."""
# ===========================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2020-2024, Daniel Krajzewicz"
__credits__    = ["Daniel Krajzewicz"]
__license__    = "BSD"
__version__    = "3.0.0"
__maintainer__ = "Daniel Krajzewicz"
__email__      = "daniel@krajzewicz.de"
__status__     = "Production"
# ===========================================================================
# - https://github.com/dkrajzew/degrotesque
# - http://www.krajzewicz.de/docs/degrotesque/index.html
# - http://www.krajzewicz.de
# ===========================================================================


# --- imports ---------------------------------------------------------------
#from . import marker
import marker


# --- variables and constants -----------------------------------------------
class DegrotesqueBeginEndMarker(marker.DegrotesqueMarker):
    def __init__(self, begin, end, extensions):
        self._begin = begin
        self._end = end
        self._extensions = extensions

        
    def get_extensions(self):
        """Returns the extensions of file types that can be processed using
        this marker.

        Returns:
            (list[str]): A list of extensions
        """
        return self._extensions
        

    def get_mask(self, document, to_skip=[]):
        """Returns a string where all text in triple quotes 
        is denoted as '0' and everything else as '1'.

        Args:
            document (str): The markdown document (contents) to process

        Returns:
            (str): Annotation of the markdown document.
        """
        length = len(document)
        ret = "1"*length
        # find opening triple quotes
        b = document.find(self._begin)
        while b>=0:
            b = b + 3
            e = b
            e = document.find(self._end, e)
            if e<0:
                raise ValueError("Not a valid document")
            ret = ret[:b] + ("0"*(e-b)) + ret[e:]
            b = document.find(self._begin, e+len(self._end))
        return ret

