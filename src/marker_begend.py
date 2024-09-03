#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ===========================================================================
"""Module holding a class that computes the mask based on a list
of beginning / closing tags as well as classes derived from this class
meant to process Python and Doxygen-documented files."""
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
class DegrotesqueBeginEndMarker(marker.DegrotesqueMarker):
    """A class that returns the mask based on a set of opening / closing
    tags.
    
    The class is initialised with a list of pairs consiting of the 
    opening / closing markers, e.g. for doxygen-documented files, items
    gets a pair consisting of '/**' and '*/' as well as one consisting
    of '///' and '\\n'.
    
    Masks all parts of a given document that are not within the opening /
    closing tags.
    """

    def __init__(self, begends, extensions, invert=False):
        self._begends = begends
        self._extensions = extensions
        self._invert = invert


    def get_extensions(self) -> List[str]:
        """Returns the extensions of file types that can be processed using
        this marker.

        Returns:
            (List[str]): A list of extensions
        """
        return self._extensions


    def get_mask(self, document : str, to_skip : List[str] = None) -> str:
        """Returns a string where all text between each of the given
        begin/end-string pairs is masked (set to '1') and everything
        else is not masted (set to '0').

        Args:
            document (str): The markdown document (contents) to process
            to_skip (List[str]): List of elements to skip (HTML/SGML/XML)

        Returns:
            (str): Annotation of the markdown document.
        """
        length = len(document)
        ret = "1"*length if not self._invert else "0"*length
        c = "0" if not self._invert else "1"
        ic = "1" if not self._invert else "0"
        #
        for be in self._begends:
            b = document.find(be[0])
            while b>=0 and b<len(document):
                if ret[b]==c:
                    b = ret.find(ic, b+1)
                    if b<0:
                        break
                    b = document.find(be[0], b+1)
                    continue
                if not be[2]:
                    b = b + len(be[0])
                e = b + len(be[0]) + 1
                e = document.find(be[1], e)
                if e<0:
                    if be[1]=="\n":
                        e = len(document)
                    else:
                        b = b + 1
                        continue
                if be[2]:
                    e = min(len(document), e + len(be[1]))
                ret = ret[:b] + (c*(e-b)) + ret[e:]
                b = document.find(be[0], e+len(be[1]))
        return self.apply_masks(document, ret)



class DegrotesquePythonMarker(DegrotesqueBeginEndMarker):
    """A class that returns the mask for a Python document.
    
    Everything is masked despite comments, excluding links.
    """

    def __init__(self):
        DegrotesqueBeginEndMarker.__init__(self, [['"""', '"""', False], ["#", "\n", False]], ["py"])



class DegrotesqueDoxygenMarker(DegrotesqueBeginEndMarker):
    """A class that returns the mask for a doxygen-documented document.
    
    Everything is masked despite doxygen comments, excluding links.
    """

    def __init__(self):
        DegrotesqueBeginEndMarker.__init__(self, [['/**', '*/', False], ["///", "\n", False]], ["java", "h", "cpp"])

