#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ===========================================================================
"""Module holding a class that computes the mask for Python documents."""
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
from typing import List
import marker_begend


# --- class definitions -----------------------------------------------------
class DegrotesquePythonMarker(marker_begend.DegrotesqueBeginEndMarker):
    """A class that returns the mask for Python documents.
    
    Code elements as well as links and references are masked.
    """

    def __init__(self):
        marker_begend.DegrotesqueBeginEndMarker.__init__(self, [['"""', '"""', False], ["#", "\n", False]], ["py"])


    def get_mask(self, document : str, to_skip : List[str] = None) -> str:
        """Returns a string where all protected text 
        is denoted as '1' and everything else as '0'.

        Args:
            document (str): The markdown document (contents) to process
            to_skip (List[str]): List of elements to skip (HTML/SGML/XML)

        Returns:
            (str): Annotation of the markdown document.
        """
        ret = marker_begend.DegrotesqueBeginEndMarker.get_mask(self, document)
        # doctest blocks
        b = document.find(">>>")
        while b>=0:
            e = document.find("\n", b)
            while e>=0 and len(document)>e+1 and not document[e+1].isspace():
                e = document.find("\n", e+1)
            if e<0:
                e = len(document)
            else:
                e = min(len(document), e+1)
            ret = ret[:b] + ("1"*(e-b)) + ret[e:]
            b = document.find(">>>", e)
        # apply standard masks (URLs, ISSN, ISBN)
        return self.apply_masks(document, ret)
            