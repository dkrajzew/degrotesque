#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ===========================================================================
"""degrotesque - Text masking class definition."""
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
from . import marker


# --- variables and constants -----------------------------------------------
class DegrotesqueTextMarker(marker.DegrotesqueMarker):
    def get_extensions(self):
        """Returns the extensions of file types that can be processed using
        this marker.

        Returns:
            (list[str]): A list of extensions
        """
        return [ "txt" ]


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
        return ret
