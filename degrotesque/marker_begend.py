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
    def __init__(self, begends, extensions):
        self._begends = begends
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
        for be in self._begends:
            b = document.find(be[0])
            while b>=0:
                b = b + len(be[0])
                e = b
                e = document.find(be[1], e)
                if e<0:
                    if be[1]=="\n":
                        e = len(document)
                    else:
                        raise ValueError("Not a valid document")
                ret = ret[:b] + ("0"*(e-b)) + ret[e:]
                b = document.find(be[0], e+len(be[1]))
        return self.mark_links(document, ret)

