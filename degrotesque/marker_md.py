#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
"""degrotesque - Markdown masking class definition."""
# =============================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2020-2024, Daniel Krajzewicz"
__credits__    = ["Daniel Krajzewicz"]
__license__    = "BSD"
__version__    = "3.0.0"
__maintainer__ = "Daniel Krajzewicz"
__email__      = "daniel@krajzewicz.de"
__status__     = "Production"
# =============================================================================
# - https://github.com/dkrajzew/degrotesque
# - http://www.krajzewicz.de/docs/degrotesque/index.html
# - http://www.krajzewicz.de
# =============================================================================


# --- imports -----------------------------------------------------------------
from . import marker



# --- variables and constants -------------------------------------------------
class DegrotesqueMDMarker(marker.DegrotesqueMarker):
    def get_mask(self, document, to_skip=[]):
        """Returns a string where all code and quotes are denoted as '1' and
        plain content as '0'.

        Args:
            document (str): The markdown document (contents) to process

        Returns:
            (str): Annotation of the markdown document.
        """
        length = len(document)
        ret = "0"*length
        # find backtick-marked code
        b = document.find("`")
        while b>=0:
            e = b + 1
            while e<length and document[e]=="`":
                e += 1
            marker = document[b:e]
            i = document.find(marker, e)
            i = length if i<0 else i+len(marker)
            ret = ret[:b] + ("1"*(i-b)) + ret[i:]
            b = document.find("`", i)
        # find indented code
        b = 0
        while b>=0 and b<length:
            e = document.find("\n", b+1)
            if e<0: e = length
            else: e += 1
            if document[b]==">" or document[b]=="\t" or (length>=b+3 and document[b:b+4]=="    "):
                ret = ret[:b] + ("1"*(e-b)) + ret[e:]
            b = e
        return ret

