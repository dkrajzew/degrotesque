#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
# ===========================================================================
"""degrotesque - A web type setter."""
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
import sys
import os
import io
import shutil
import re
from typing import List
from typing import Union
import argparse
import configparser
import helper
import marker
import marker_text
import marker_md
import marker_html
import marker_begend
import marker_rst


# --- variables and constants -----------------------------------------------
# A database of actions
actions_db = {
    # english quotes
    "quotes.english": [
        [[u"(\\s+)'", u"'"],             [u"\\1&#8216;", u"&#8217;"]],
        [[u"\"", u"\""],                 [u"&#8220;", u"&#8221;"]]
    ],

    # french quotes
    "quotes.french": [
        [[u"&lt;&lt;", u"&gt;&gt;"],     [u"&#x00AB;", u"&#x00BB;"]],
        [[u"&lt;", u"&gt;"],             [u"&#x2039;", u"&#x203A;"]]
    ],

    # german quotes
    "quotes.german": [
        [[u"(\\s+)'", u"'"],             [u"\\1&#x201A;", u"&#x2019;"]],
        [[u"\"", u"\""],                 [u"&#x201E;", u"&#x201D;"]]
    ],

    # conversion to HTML quotes (<q>)
    "to_quotes": [
        [[u"(\\s+)'", u"'"],             [u"\\1<q>", u"</q>"]],
        [[u"\"", u"\""],                 [u"<q>", u"</q>"]],
        [[u"&lt;&lt;", u"&gt;&gt;"],     [u"<q>", u"</q>"]],
        [[u"&lt;", u"&gt;"],             [u"<q>", u"</q>"]]
    ],

    # commercial signs
    "commercial": [
        [[u"\\([c|C]\\)", None],         [u"&#169;", None]],
        [[u"\\([r|R]\\)", None],         [u"&#174;", None]],
        [[u"\\([t|T][m|M]\\)", None],    [u"&#8482;", None]]
    ],

    # dashes
    "dashes": [
        # missing: ndash for number ranges
        [[u"(\\s+)-(\\s+)", None],       [u"\\1&#8212;\\2", None]],
        [[u"([\\d]+)-([\\d]+)", None],   [u"\\1&#8211;\\2", None]]
    ],

    # arrows
    "arrows": [
        [[u"<-", None],      [u"\\1&#8592;\\2", None]],
        [[u"<--", None],     [u"\\1&#8592;\\2", None]],
        [[u"->", None],      [u"\\1&#8594;\\2", None]],
        [[u"-->", None],     [u"\\1&#8594;\\2", None]],
        [[u"<=", None],      [u"\\1&#8656;\\2", None]],
        [[u"<==", None],     [u"\\1&#8656;\\2", None]],
        [[u"=>", None],      [u"\\1&#8658;\\2", None]],
        [[u"==>", None],     [u"\\1&#8658;\\2", None]]
    ],

    # bullets
    "bullets": [
        [[u"\\*", None],                 [u"&#8226;", None]]
    ],

    # ellipsis
    "ellipsis": [
        [[u"\\.\\.\\.", None],           [u"&#8230;", None]]
    ],

    # apostrophe
    "apostrophe": [
        [[u"'", None],                   [u"&#39;", None]]
    ],

    # dagger
    "dagger": [
        [[u"\\*\\*", None],              [u"&#8225;", None]],
        [[u"\\*", None],                 [u"&#8224;", None]]
    ],

    # math signs
    "math": [
        [[u"\\+/-", None],               [u"&#177;", None]],
        [[u"1/2", None],                 [u"&#189;", None]],
        [[u"1/4", None],                 [u"&#188;", None]],
        [[u"3/4", None],                 [u"&#190;", None]],
        [[u"\\~", None],                 [u"&#8776;", None]],
        [[u"\\!=", None],                [u"&#8800;", None]],
        [[u"&lt;=", None],               [u"&#8804;", None]],
        [[u"&gt;=", None],               [u"&#8805;", None]],
        [[u"([\\d]+)(\\s*)\\*(\\s*)([\\d]+)", None],  [u"\\1\\2&#215;\\3\\4", None]],
        [[u"([\\d]+)(\\s*)x(\\s*)([\\d]+)", None],    [u"\\1\\2&#215;\\3\\4", None]],
        [[u"([\\d]+)(\\s*)/(\\s*)([\\d]+)", None],    [u"\\1\\2&#247;\\3\\4", None]]
    ],

    # chem
    "chem": [
        [[u"([a-zA-Z]+)([\\d]+)", None],        [u"\\1<sub>\\2</sub>", None]]
    ]
}


# Mapping Unicode to HTML entities
encoding_map = {
    "&#8216;"   : [ "&lsquo;" ],
    "&#8217;"   : [ "&rsquo;" ],
    "&#8220;"   : [ "&ldquo;" ],
    "&#8221;"   : [ "&rdquo;" ],
    "&#x00AB;"  : [ "&laquo;" ],
    "&#x00BB;"  : [ "&raquo;" ],
    "&#x2039;"  : [ "&lsaquo;" ],
    "&#x203A;"  : [ "&rsaquo;" ],
    "&#x201A;"  : [ "&sbquo;" ],
    "&#x2019;"  : [ "&rsquo;" ],
    "&#x201E;"  : [ "&bdquo;" ],
    "&#x201D;"  : [ "&rdquo;" ],
    "&#169;"    : [ "&copy;" ],
    "&#174;"    : [ "&reg;" ],
    "&#8482;"   : [ "&trade;" ],
    "&#8212;"   : [ "&mdash;" ],
    "&#8211;"   : [ "&ndash;" ],
    "&#8226;"   : [ "&bull;" ],
    "&#8230;"   : [ "&hellip;" ],
    "&#39;"     : [ "&apos;" ],
    "&#8225;"   : [ "&Dagger;" ],
    "&#8224;"   : [ "&dagger;" ],
    "&#177;"    : [ "&plusmn;" ],
    "&#189;"    : [ "&frac12;" ],
    "&#188;"    : [ "&frac14;" ],
    "&#190;"    : [ "&frac34;" ],
    "&#8776;"   : [ "&asymp;" ],
    "&#8800;"   : [ "&ne;" ],
    "&#8804;"   : [ "&le;" ],
    "&#8805;"   : [ "&ge;" ],
    "&#215;"    : [ "&times;" ],
    "&#247;"    : [ "&divide;" ],
    "&#8592;"   : [ "&larr;" ],
    "&#8594;"   : [ "&rarr;" ],
    "&#8656;"   : [ "&lArr;" ],
    "&#8658;"   : [ "&rArr;" ]
}


# --- functions -------------------------------------------------------------
# --- replacement functions
def _replace_keep(matchobj : re.Match) -> str:
    """Unicode numbers conversion to itself

    Args:
        matchobj (Match): The match object to get a new representation for

    Returns:
        (str): The converted string (here: as Unicode number)
    """
    return matchobj.group(0)


def _replace_html(matchobj : re.Match) -> str:
    """Unicode numbers conversion to HTML entities

    Args:
        matchobj (Match): The match object to get a new representation for

    Returns:
        (str): The converted string (here: as HTML entity)
    """
    return encoding_map[matchobj.group(0)][0]


def _replace_unicode(matchobj : re.Match) -> str:
    """Unicode numbers conversion to Unicode characters

    Args:
        matchobj (Match): The match object to get a new representation for

    Returns:
        (str): The converted string (here: as Unicode character)
    """
    c = matchobj.group(0)[2]
    if c=='x' or c=='X':
        return chr(int("0" + matchobj.group(0)[2:-1], 16))
    return chr(int(matchobj.group(0)[2:-1]))



# --- class definitions -----------------------------------------------------
class Degrotesque:
    """A tiny web type setter.

    The main method "prettify" uses the list of actions to change the
    contents of the given HTML page.

    XML-elements are skipped as well as the contents of specific elements.
    Additional methods support parsing and setting new values for actions
    and elements to skip.

    Some internal methods exist for determining which parts of the document
    shall processed and which ones shall be skipped.
    """

    # --- init
    def __init__(self):
        """Sets defaults for the elements which contents shall not be
        processed.

        Sets defaults for actions to perform.
        """
        # the actions to apply
        self._restore_default_actions()
        # the target format converter
        self._replace_func = _replace_keep
        # the target format regexp
        self._target_regex = re.compile("(&#[xX]?[0-9a-fA-F]*;)")
        # set up markers
        self._markers = {}
        self._markers["text"] = marker_text.DegrotesqueTextMarker()
        self._markers["md"] = marker_md.DegrotesqueMDMarker()
        self._markers["sgml"] = marker_html.DegrotesqueHTMLMarker()
        self._markers["python"] = marker_begend.DegrotesquePythonMarker()
        self._markers["doxygen"] = marker_begend.DegrotesqueDoxygenMarker()
        self._markers["rst"] = marker_rst.DegrotesqueRSTMarker()


    def _restore_default_actions(self):
        """Instantiates default actions"""
        self.set_actions("quotes.english,dashes,ellipsis,math,apostrophe,commercial")


    def set_actions(self, action_names : List[str]):
        """Sets the actions to apply.

        If the given names of actions are None or empty, the default actions
        are used.

        Otherwise, the actions matching the given names are retrieved from the
        internal database and their list is returned.

        Args:
            action_names (List[str]): The names of the actions to use (or None if default actions shall be used)
        """
        if action_names is None or len(action_names)==0:
            return
        action_names = action_names.split(",")
        self._actions = []
        for an in action_names:
            if an not in actions_db:
                raise ValueError("action '%s' is not known" % (an))
            for a in actions_db[an]:
                n = list(a)
                n[0][0] = re.compile(n[0][0])
                if n[0][1] is not None:
                    n[0][1] = re.compile(n[0][1])
                self._actions.append(n)


    def set_format(self, format_name : str):
        """Sets the target character representation

        Args:
            format_name (str): The format to use, one of "html", "unicode", "text"
        """
        if format_name=="html":
            self._replace_func = _replace_html
        elif format_name=="unicode":
            self._replace_func = _replace_keep
        elif format_name=="text":
            self._replace_func = _replace_unicode
        else:
            raise ValueError("Unknown target format '%s'" % format_name)


    def get_marker(self, filename : str, document : str) -> marker.DegrotesqueMarker:
        """Returns the marker to use.

        In a first step, the marker to use is tried to be determined using
        the file's extension. If the extension matches a marker, this
        marker is returned.

        If the extension is not listed in the markers' extensions lists,
        it is tried to check whether it is a SGML derivative (HTML/XML/...).
        In this case, a DegrotesqueHTMLMarker is returned.

        If no other marker could be found, a DegrotesqueTextMarker is
        returned.

        Args:
            filename (str): The name / path of the file
            document (str): The file's contents
        """
        name, ext = os.path.splitext(filename)
        ext = ext[1:]
        tmarker = None
        for m in self._markers:
            if ext in self._markers[m].get_extensions():
                return self._markers[m]
        # the HTML recognition regexp
        document = document.strip().lower()
        if document.startswith("<?xml") or document.startswith("<!doctype"):
            return self._markers["sgml"]
        if document.startswith("<") and document.endswith(">"):
            return self._markers["sgml"]
        return self._markers["text"]



    def prettify(self, document : str, marker : marker.DegrotesqueMarker) -> str:
        """Prettifies (degrotesques) the given document.

        It is assumed that the input is given in utf-8.

        The result is returned in utf-8 as well.

        Args:
            document (str): The document (contents) to process.
            marker (marker.DegrotesqueMarker): The marker object to use for computing the mask of document parts to skip

        Returns:
            (str): The processed (prettified / degrotesqued) document.
        """
        # extract text parts
        marks = marker.get_mask(document)
        assert(len(document)==len(marks))
        # build a copy of actions to use (not found will be removed from it)
        actions = list(self._actions)
        # add placeholder for opening / closing regexp
        for a in actions:
            a.append(None)
            a.append(None)
        # start processing
        pos = 0
        while pos<len(document) and len(actions)>0:
            nactions = []
            # go through actions, find next occurrence of each
            # (both - opening and closing regexp must be found, if a closing exists)
            for a in actions:
                bpos = pos
                opening = a[0][0].search(document[bpos:])
                while opening and marks[bpos+opening.start():bpos+opening.end()].find("1")>=0:
                    bpos = bpos + opening.start() + 1
                    opening = a[0][0].search(document[bpos:])
                if not opening:
                    continue
                bpos = bpos + opening.start()
                epos = bpos + opening.end() - opening.start()
                closing = None
                if a[0][1] is not None:
                    closing = a[0][1].search(document[epos:])
                    while closing and marks[epos+closing.start():epos+closing.end()].find("1")>=0:
                        epos = epos + closing.start() + 1
                        closing = a[0][1].search(document[epos:])
                    if not closing:
                        continue
                    epos = epos + closing.start()
                a[-2] = [opening, bpos]
                a[-1] = [closing, epos]
                nactions.append(a)
            # no actions found - break
            if len(nactions)==0:
                break
            # get the next one
            nactions.sort(key=lambda t: t[-2][1])
            a = nactions[0]
            opening, bpos = a[-2]
            closing, epos = a[-1]
            # perform replacement
            if closing is not None:
                closing = a[0][1].match(document[epos:])
                dest = self._target_regex.sub(self._replace_func, a[1][1])
                tmp = a[0][1].sub(dest, document[epos:], 1)
                replacement_length = closing.end() - closing.start() + len(tmp) - len(document[epos:])
                document = document[:epos] + tmp
                marks = marks[:epos+closing.start()] + "1"*replacement_length + marks[epos+closing.end():]
                assert (len(document)==len(marks))
            opening = a[0][0].match(document[bpos:])
            dest = self._target_regex.sub(self._replace_func, a[1][0])
            tmp = a[0][0].sub(dest, document[bpos:], 1)
            replacement_length = opening.end() + len(tmp) - len(document[bpos:])
            document = document[:bpos] + tmp
            marks = marks[:bpos] + "1"*replacement_length + marks[bpos+opening.end():]
            assert (len(document)==len(marks))
            # move in document, adapt actions list (found only)
            pos = bpos + opening.end() + 1
            actions = nactions
        return document


# --- functions -------------------------------------------------------------
def prettify(document : str, marker : Union[marker.DegrotesqueMarker, str] = None, actions : Union[List[str], str] = None, to_skip : Union[List[str], str] = None, replacement_format : str = "text") -> str:
    """Prettifies (degrotesques) the given document.

    Builds a Degrotesque instance, inserts the given options, 
    and applies it on the document.

    Args:
        document (str): The document (contents) to process.
        marker (Union[marker.DegrotesqueMarker, str]): The marker object to use for computing the mask of document parts to skip or its name
        actions (Union[List[str], str]): The named actions to perform; if given as string, they must be separated using a colon (,)
        to_skip (Union[List[str], str]): The HTML-elements to skip; if given as string, they must be separated using a colon (,)
        replacement_format (str): The type of replacements to use, one of 'html', 'text', 'unicode'

    Returns:
        (str): The processed (prettified / degrotesqued) document.
    """
    degrotesque = Degrotesque()
    if actions is not None:
        if isinstance(actions, list):
            actions = ",".join(actions)
        degrotesque.set_actions(actions)
    if to_skip is not None:
        if isinstance(to_skip, list):
            to_skip = ",".join(to_skip)
        degrotesque._markers["sgml"].set_to_skip(to_skip)
    degrotesque.set_format(replacement_format)
    if isinstance(marker, str):
        marker = degrotesque._markers[marker]
    return degrotesque.prettify(document, marker)
    

def main(arguments : List[str] = []) -> int:
    """The main method using parameter from the command line.

    The application reads the given file or the files from the folder (optionally
    recursive) defined by the -i/--input option. If -r/--recursive option is set,
    the input folder will be scanned recursively. All files are processed but can
    be limited to those that match the extension defined using the -e/--extension
    option. The default encoding for the files is utf-8. This can be changed
    using the -E/--encoding option.

    The default actions or those named using the -a/--actions option are
    applied. When parsing HTML documents, elements are skipped. The contents of
    default elements to skip or those defined using -s/--skip are skipped as well.
    degrotesque tries to determine the file type using the respective extension.
    The options -T/--text, -H/--html, and -M/--markdown overwrite this behaviour.

    The target format of the replacements is unicode entity but may be changed
    using the -f/--format option.

    The files are saved under their original name. If the option -B/--no-backup is not
    given, a backup of the original files is generated named as the original
    file with the appendix ".orig".


    Args:
        arguments (List[str]): The command line arguments, parsed as options using OptionParser.

    Options
    -------

    The following options must be set:

    --input / -i _&lt;FILE or FOLDER NAME&gt;_:
        the file or the folder to process

    The following options are optional:

    --recursive / -r:
        Set if the folder — if given — shall be processed recursively

    --extensions / -e _&lt;EXTENSION&gt;[,&lt;EXTENSION&gt;]\*_:
        The extensions of files that shall be processed

    --encoding / -E _&lt;ENCODING&gt;_:
        File encoding (default: 'utf-8')

    --html / -H:
        Files are HTML/XML-derivatives

    --text / -T:
        Files are plain text files

    --markdown / -M:
        Files are markdown files

    --no-backup / -B:
        Set if no backup files shall be generated

    --format / -f _&lt;FORMAT&gt;_:
        Define the format of the replacements ['html', 'unicode', 'text']

    --skip / -s _&lt;ELEMENT_NAME&gt;[,&lt;ELEMENT_NAME&gt;]\*_:
        Elements which contents shall not be changed

    --actions / -a _&lt;ACTION_NAME&gt;[,&lt;ACTION_NAME&gt;]\*_:
        Name the actions that shall be applied

    --help / -h:
        Prints the help screen

    --version / -v:
        Prints the version

    """
    # parse options
    # https://stackoverflow.com/questions/3609852/which-is-the-best-way-to-allow-configuration-options-be-overridden-at-the-comman
    defaults = {}
    conf_parser = argparse.ArgumentParser(prog='degrotesque', add_help=False)
    conf_parser.add_argument("-c", "--config", metavar="FILE", help="Reads the named configuration file")
    args, remaining_argv = conf_parser.parse_known_args(arguments)
    if args.config is not None:
        if not os.path.exists(args.config):
            print ("degrotesque: error: configuration file '%s' does not exist" % str(args.config), file=sys.stderr)
            raise SystemExit(2)
        config = configparser.ConfigParser()
        config.read([args.config])
        defaults.update(dict(config.items("DEFAULT")))
    parser = argparse.ArgumentParser(prog='degrotesque', parents=[conf_parser], 
        description='A type setter that exchanges ascii letters by their typographic counterparts', 
        epilog='(c) Daniel Krajzewicz 2020-2024')
    parser.add_argument("input")
    parser.add_argument('--version', action='version', version='%(prog)s 3.0.0')
    parser.add_argument("-r", "--recursive", action="store_true", default=False, help="Whether a given path shall be processed recursively")
    parser.add_argument("-e", "--extensions",default=None, help="Defines the extensions of files to process")
    parser.add_argument("-E", "--encoding", default="utf-8", help="File encoding (default: 'utf-8')")
    parser.add_argument("-T", "--type", choices=['sgml', 'text', 'md', 'doxygen', 'python', 'rst'], help="Name the file type, one of  ['sgml', 'text', 'md', 'doxygen', 'python', 'rst']")
    parser.add_argument("-B", "--no-backup", dest="no_backup", action="store_true", help="Whether no backup shall be generated")
    parser.add_argument("-f", "--format", choices=['html', 'unicode', 'text'], default="unicode", help="Defines the format of the replacements ['html', 'unicode', 'text']")
    parser.add_argument("-s", "--skip", default=None, help="Defines the elements which contents shall not be changed")
    parser.add_argument("-w", "--write-config", metavar="FILE", help="Writes the current settings to the named configuration file")
    parser.add_argument("-a", "--actions", default=None, help="Defines the actions to perform")
    parser.set_defaults(**defaults)
    args = parser.parse_args(remaining_argv)
    # setup degrotesque
    degrotesque = Degrotesque()
    try:
        degrotesque.set_actions(args.actions)
    except ValueError as err:
        parser.print_usage(sys.stderr)
        print ("degrotesque: error: argument -a/--actions: %s" % str(err), file=sys.stderr)
        raise SystemExit(2)
    degrotesque._markers["sgml"].set_to_skip(args.skip)
    degrotesque.set_format(args.format)
    # get marker
    marker = None
    if args.type is not None:
        marker = degrotesque._markers[args.type]
    # write config
    if args.write_config:
        tmp_args = vars(args).copy()
        with open(args.write_config, "w") as fdo:
            fdo.write("[DEFAULT]\n")
            for arg in tmp_args:
                if arg=="write_config" or arg=="config" or tmp_args[arg] is None:
                    continue
                fdo.write("%s=%s\n" % (arg, tmp_args[arg]))
    # collect files
    extensions = helper.get_extensions(args.extensions)
    try:
        files = helper.get_files(args.input, args.recursive, extensions)
    except ValueError as err:
        parser.print_usage(sys.stderr)
        print ("degrotesque: error: %s" % str(err), file=sys.stderr)
        raise SystemExit(2)
    # loop through files
    for f in files:
        print("Processing %s" % f)
        try:
            # read the file
            with io.open(f, mode="r", encoding=args.encoding) as fd:
                document = fd.read()
            # get the contents marker to use
            tmarker = marker
            if tmarker is None:
                tmarker = degrotesque.get_marker(f, document)
            # apply the beautifications
            document = degrotesque.prettify(document, tmarker)
            # build a backup
            if not args.no_backup:
                shutil.copy(f, f+".orig")
            # save the new contents
            with io.open(f, mode="w", encoding=args.encoding) as fd:
                fd.write(document)
        except ValueError as err:
            print(str(err))
            return 4
    return 0


# -- main check
if __name__ == '__main__':
    ret = main(sys.argv[1:]) # pragma: no cover
    sys.exit(ret) # pragma: no cover
