#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ===========================================================================
"""degrotesque - base marker class definition."""
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
import re


# --- variables and constants -----------------------------------------------
class DegrotesqueMarker(metaclass=ABCMeta):
    @abstractmethod
    def get_extensions(self):
        """Returns the extensions of file types that can be processed using
        this marker.

        Returns:
            (list[str]): A list of extensions
        """
        pass # pragma: no cover


    @abstractmethod
    def get_mask(self, document, to_skip=[]):
        """Returns a string where all parts to exclude from replacements
        denoted as '1' and all with plain content that shall be processed
        as '0'.

        Args:
            document (str): The document (contents) to process

        Returns:
            (str): Annotation of the document.
        """
        pass # pragma: no cover


    def mark_links(self, document, mask):
        # https://stackoverflow.com/questions/6718633/python-regular-expression-again-match-url
        mre = re.compile("((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*")
        res = mre.finditer(document)
        for r in res:
            f = "1" * (r.end()-r.start())
            mask = mask[:r.start()] + f + mask[r.end():]
        return mask
