#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ===========================================================================
""""Module holding a class that computes the mask for Markdown documents."""
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
import re
import marker


# --- class definitions -----------------------------------------------------
class DegrotesqueMDMarker(marker.DegrotesqueMarker):
    """A class that returns the mask for markdown text.
    
    Code elements - indented and ones that use tripe-` are
    masked as well as links.
    """

    def get_extensions(self) -> List[str]:
        """Returns the extensions of file types that can be processed using
        this marker.

        Returns:
            (List[str]): A list of extensions
        """
        return [ "md" ]


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
        # mask markdown links
        # https://stackoverflow.com/questions/67940820/how-to-extract-markdown-links-with-a-regex
        expr = re.compile(f'\[[^\[]+]\((\s*.+\s*)\)')
        for r in expr.finditer(document):
            f = "1" * (r.end(1)-r.start(1))
            ret = ret[:r.start(1)] + f + ret[r.end(1):]
        expr = re.compile(f'\<http[s]?://.+?\>')
        for r in expr.finditer(document):
            f = "1" * (r.end()-r.start())
            ret = ret[:r.start()] + f + ret[r.end():]
        # apply standard masks (URLs, ISSN, ISBN)
        return self.apply_masks(document, ret)

