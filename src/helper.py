#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ===========================================================================
"""Module with some helper functions."""
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
import os
from typing import List


# --- functions -------------------------------------------------------------
def get_extensions(names : List[str]) -> List[str]:
    """Returns the list of extensions of files to process.

    If the given names of extensions are None or empty, the default
    extensions are used.

    Otherwise, the given string is split and returned as a list.

    Args:
        names (List[str]): The names of extensions to process (or None if default extensions shall be used)

    Returns:
        (List[str]): The list of extensions to use.

    todo:
        What about removing dots?
    """
    if names is None or len(names)==0:
        return None
    exts = [x.strip() for x in names.split(',')]
    if "*" in exts:
        return None
    return exts


def get_files(name : str, recursive : bool, extensions : List[str]) -> List[str]:
    """Returns the files to process.

    If a file name is given, a list with only this file name is returned.

    If a folder name is given, the files to process are determined by walking
    through the folder — recursively if wished — and collecting all files
    that match the extensions.

    The list of collected files is returned.

    Args:
        name (str): The name of the file/folder
        recursive (bool): Whether the folder (if given) shall be processed recursively
        extensions (List[str]): The extensions of the files to process

    Returns:
        (List[str]): The list of collected files.
    """
    files = []
    if os.path.isdir(name):
        for root, dirs, dfiles in os.walk(name):
            for f in dfiles:
                n, e = os.path.splitext(os.path.join(root, f))
                if extensions is not None and len(extensions)!=0 and e[1:] not in extensions:
                    continue
                files.append(os.path.join(root, f))
            if not recursive:
                break
    elif os.path.isfile(name):
        files.append(name)
    else:
        raise ValueError("can not process '%s'" % name) # pragma: no cover
    files.sort()
    files.sort(key=lambda v: str(v).replace("\\", "/").count('/'))
    return files


def get_default_to_skip():
    return [
        u"script", u"code", u"style", u"pre", u"samp", u"tt", u"kbd",
        u"?", u"?php",
        u"%", u"%=", u"%@", u"%--", u"%!",
        u"!--", "!doctype"
    ]


def parse_to_skip(to_skip : List[str]):
    """Sets the elements which contents shall not be changed.

    Otherwise, a list with the elements to skip is built.

    Args:
        elements_to_skip (List[str]): The names of elements which shall not be changed

    Todo:
        Warn user if a non-XML-character occurs?
    """
    if to_skip is None or len(to_skip)==0:
        return get_default_to_skip()
    if isinstance(to_skip, list):
        to_skip = ",".join(to_skip)
    return [x.strip() for x in to_skip.split(',')]
    