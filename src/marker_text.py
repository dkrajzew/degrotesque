#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ===========================================================================
""""Module holding the base class that comoputes the mask for plain text
documents."""
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
import marker


# --- class definitions -----------------------------------------------------
class DegrotesqueTextMarker(marker.DegrotesqueMarker):
    """A class that returns the mask for plain text.
    
    Only links are masked out, everything else can be changed.
    """

    def get_extensions(self) -> List[str]:
        """Returns the extensions of file types that can be processed using
        this marker.

        Returns:
            (list[str]): A list of extensions
        """
        return [ "txt" ]


    def get_mask(self, document : str) -> str:
        """Returns a string where all code and quotes are denoted as '1' and
        plain content as '0'.

        Args:
            document (str): The markdown document (contents) to process

        Returns:
            (str): Annotation of the markdown document.
        """
        length = len(document)
        ret = "0"*length
        return self.apply_masks(document, ret)
