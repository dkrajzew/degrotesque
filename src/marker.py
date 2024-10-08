#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ===========================================================================
"""Module holding the base class for computing the mask holding
document parts not to process."""
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
from abc import ABCMeta, abstractmethod
from typing import List
import re


# --- class definitions -----------------------------------------------------
class DegrotesqueMarker(metaclass=ABCMeta):
    """The base class for computing the mask holding document parts not to
    process."""

    @abstractmethod
    def get_extensions(self) -> List[str]:
        """Returns the extensions of file types that can be processed using
        this marker.

        Returns:
            (List[str]): A list of extensions
        """
        pass # pragma: no cover


    @abstractmethod
    def get_mask(self, document : str, to_skip : List[str] = None) -> str:
        """Returns a string where all parts to exclude from replacements
        denoted as '1' and all with plain content that shall be processed
        as '0'.

        Args:
            document (str): The document (contents) to process
            to_skip (List[str]): List of elements to skip (HTML/SGML/XML)

        Returns:
            (str): Annotation of the document.
        """
        pass # pragma: no cover


    def apply_masks(self, document : str, mask : str) -> str:
        """Masks (sets the contents of the mask to '1') all URLs and
        ISSN / ISBN.
        
        The method is assumed to be called after an initial mask has been 
        computed.

        Args:
            document (str): The document (contents) to process
            mask (str): A previously computed mask

        Returns:
            (str): Annotation of the document.
        """
        # mask URLs
        # https://stackoverflow.com/questions/6718633/python-regular-expression-again-match-url
        mre = re.compile("((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*")
        res = mre.finditer(document)
        for r in res:
            f = "1" * (r.end()-r.start())
            mask = mask[:r.start()] + f + mask[r.end():]
        # mask ISSN and ISBN numbers
        for to_mask in [
                "978-[\d]+-[\d]+-[\d]+-[\d]", "979-[\d]+-[\d]+-[\d]+-[\d]",
                "[\d]+-[\d]+-[\d]+-[\d]+", "ISSN \d{4}-\d{4}"
                ]:
            mre = re.compile(to_mask)
            res = mre.finditer(document)
            for r in res:
                f = "1" * (r.end()-r.start())
                mask = mask[:r.start()] + f + mask[r.end():]
        return mask
