#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ===========================================================================
""""Module holding a class that computes the mask for HTML documents."""
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
class DegrotesqueHTMLMarker(marker.DegrotesqueMarker):
    """A class that returns the mask for SGML (HTML/XML) documents.
    
    Masks all element (opening, closing, single) element definitions
    and everything else that is within < and >. Masks the contents of code
    elements (<pre>, <code> and others). Masks links.
    """
    
    def __init__(self):
        self._restore_default_elements_to_skip()
        

    def get_extensions(self) -> List[str]:
        """Returns the extensions of file types that can be processed using
        this marker.

        Returns:
            (List[str]): A list of extensions
        """
        return [
            "html", "htm", "xhtml",
            "php", "phtml", "phtm", "php2", "php3", "php4", "php5",
            "asp",
            "jsp", "jspx",
            "shtml", "shtm", "sht", "stm",
            "vbhtml", "ppthtml", "ssp", "jhtml",
            "xml", "osm"
        ]


    def get_mask(self, document : str) -> str:
        """Returns a string where all HTML-elements are denoted as '1' and
        plain content as '0'.

        Args:
            document (str): The HTML document (contents) to process

        Returns:
            (str): Annotation of the HTML document.
        """
        # mark HTML elements
        ldocument = document.lower()
        ret = ""
        i = 0
        while i<len(ldocument):
            if ldocument[i]=='<':
                ret = ret + "1"
            elif ldocument[i]=='>':
                ret = ret + "1"
                i += 1
                continue
            else:
                ret = ret + "0"
                i += 1
                continue
            # process elements to skip contents of
            i += 1
            tb = self._get_tag_name(ldocument[i:])
            ret += "1"*(len(tb))
            i = i + len(tb)
            if tb not in self._elements_to_skip:
                ie = ldocument.find(">", i)
                if ie<0:
                    raise ValueError("Unclosed element at %s" % (i-len(tb)))
                ret += "1"*(ie-i+1)
                i = ie + 1
                continue
            ib = i
            if tb=="?" or tb=="?php":
                # assumption: php stuff is always closed by ?>
                ie = ldocument.find("?>", ib)
                if ie<0: raise ValueError("Unclosed '<%s' element at position %s." % (tb, i))
                ie += 1
            elif tb=="%" or tb=="%=" or tb=="%@" or tb=="%--" or tb=="%!":
                # assumption: jsp/asp stuff is always closed by %>
                ie = ldocument.find("%>", ib)
                if ie<0: raise ValueError("Unclosed '<%s' element at position %s." % (tb, i))
                ie += 1
            elif tb=="!--":
                # comments are always closed by -->
                ie = ldocument.find("-->", ib)
                if ie<0: raise ValueError("Unclosed '<%s' element at position %s." % (tb, i))
                ie += 2
            elif tb=="!doctype":
                # DOCTYPE: find matching >
                ie = ib+1
                num = 1
                while ie<len(ldocument):
                    if ldocument[ie]=="<": num = num + 1
                    elif ldocument[ie]==">": num = num + 1
                    if num==0: break
                    ie = ie + 1
                ie -= 1
            else:
                # everything else (code, script, etc. that may contain < or >) should
                # be parsed until a closing tag
                # but: you may find <code> in <code>!?
                num = 1
                ie = i + 1
                while True:
                    ie1 = ldocument.find("</"+tb, ie)
                    ie2 = ldocument.find("<"+tb, ie)
                    if ie1<0 and ie2<0:
                        raise ValueError("Unclosed '<%s' element at position %s." % (tb, i))
                    if ie1>=0 and (ie1<ie2 or ie2<0):
                        num = num - 1
                        ie = ie1 + len("</"+tb)
                    if ie2>=0 and (ie2<ie1 or ie1<0):
                        num = num + 1
                        ie = ie2 + len("<"+tb)
                    if num==0: break
            ret += "1"*(ie-ib)
            i = ie
        assert (len(ret)==len(ldocument))
        return self.apply_masks(document, ret)



    def _restore_default_elements_to_skip(self):
        """Instantiates default elements to skip"""
        # list of elements which contents shall not be processed
        self._elements_to_skip = [
            u"script", u"code", u"style", u"pre", u"samp", u"tt", u"kbd",
            u"?", u"?php",
            u"%", u"%=", u"%@", u"%--", u"%!",
            u"!--", "!doctype"
        ]


    def set_to_skip(self, elements_to_skip : List[str]):
        """Sets the elements which contents shall not be changed.

        If the given names of elements are None or empty, the default elements
        to skip are used.

        Otherwise, a list with the elements to skip is built.

        Args:
            elements_to_skip (List[str]): The names of elements which shall not be changed

        Todo:
            Warn user if a non-XML-character occurs?
        """
        if elements_to_skip is None or len(elements_to_skip)==0:
            return
        self._elements_to_skip = [x.strip() for x in elements_to_skip.split(',')]
        
        
    def _get_tag_name(self, document : str) -> str:
        """Returns the name of the tag that starts at the begin of the given string.

        Args:
            document (str): The HTML-subpart

        Returns:
            (str): The name of the tag
        """
        i = 0
        while i<len(document) and (ord(document[i])<=32 or document[i]=="/"):
            i = i + 1
        ib = i
        ie = i
        while ie<len(document) and document[ie] not in " \n\r\t>/":
            ie += 1
        return document[ib:ie]
