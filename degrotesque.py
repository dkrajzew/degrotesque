from __future__ import print_function
# ===================================================================
# degrotesque - A web type setter.
#
# Main module
#
# (c) Daniel Krajzewicz 2020-2023
# daniel@krajzewicz.de
# - https://github.com/dkrajzew/degrotesque
# - http://www.krajzewicz.de/docs/degrotesque/index.html
# - http://www.krajzewicz.de
#
# Available under the BSD license.
# ===================================================================


# --- imports -------------------------------------------------------
import sys
import os
import io
import shutil
import re
from optparse import OptionParser



# --- variables and constants ---------------------------------------
# A database of actions
actionsDB = {
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
    ],

    # masks
    "masks": [
        [[u"978-([\\d]+)-([\\d]+)-([\\d]+)-([\\d])(\\D)", None], [u"978-\\1-\\2-\\3-\\4\\5", None]],
        [[u"979-([\\d]+)-([\\d]+)-([\\d]+)-([\\d])(\\D)", None], [u"979-\\1-\\2-\\3-\\4\\5", None]],
        [[u"([\\d]+)-([\\d]+)-([\\d]+)-([\\d])(\\D)", None],     [u"\\1-\\2-\\3-\\4\\5", None]],
        [[u"ISSN (\\d{4})-(\\d{4})(\\D)", None],                 [u"ISSN \\1-\\2\\3", None]]
    ]
}


# A database of extensions of HTML derivatives
htmlExtensions = [
    "html", "htm", "xhtml",
    "php", "phtml", "phtm", "php2", "php3", "php4", "php5",
    "asp",
    "jsp", "jspx",
    "shtml", "shtm", "sht", "stm",
    "vbhtml", "ppthtml", "ssp", "jhtml",
    "xml", "osm"
]


# A database of markdown file extensions
markdownExtensions = [ "md" ]


# Mapping Unicode to HTML entities
encodingMap = {
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
    "&#247;"    : [ "&divide;" ]

}


# --- _replFunc_keep
def _replFunc_KEEP(matchobj):
    """Unicode numbers conversion to itself

    Args:
        matchobj (Match): The match object to get a new representation for
    
    Returns:
        (str): The converted string (here: as Unicode number)
    """
    return matchobj.group(0)


def _replFunc_HTML(matchobj):
    """Unicode numbers conversion to HTML entities

    Args:
        matchobj (Match): The match object to get a new representation for
    
    Returns:
        (str): The converted string (here: as HTML entity)
    """
    return encodingMap[matchobj.group(0)][0]


def _replFunc_UNICODE(matchobj):
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



# --- class ---------------------------------------------------------
class Degrotesque():
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
        # the elements to skip
        self._restoreDefaultElementsToSkip()
        # the actions to apply
        self._restoreDefaultActions()
        # the target format converter
        self._replFunc = _replFunc_KEEP
        # the target format regexp
        self._targetRegex = re.compile("(&#[xX]?[0-9a-fA-F]*;)")


    # --- restoreDefaultActions
    def _restoreDefaultActions(self):
        """Instantiates default actions"""
        self.setActions("masks,quotes.english,dashes,ellipsis,math,apostrophe,commercial")


    # --- setActions
    def setActions(self, actNames):
        """Sets the actions to apply.

        If the given names of actions are None or empty, the default actions
        are used.

        Otherwise, the actions matching the given names are retrieved from the
        internal database and their list is returned.

        Args:
            actNames (List[str]): The names of the actions to use (or None if default actions shall be used)
        """
        if actNames is None or len(actNames)==0:
            return
        actNames = actNames.split(",")
        self._actions = []
        for an in actNames:
            if an not in actionsDB:
                raise ValueError("Action '%s' is not known." % (an))
            for a in actionsDB[an]:
                n = list(a)
                n[0][0] = re.compile(n[0][0])
                if n[0][1] is not None:
                    n[0][1] = re.compile(n[0][1])
                self._actions.append(n)
                


    # --- restoreDefaultActions
    def _restoreDefaultElementsToSkip(self):
        """Instantiates default elements to skip"""
        # list of elements which contents shall not be processed
        self._elementsToSkip = [
            u"script", u"code", u"style", u"pre", u"?", u"?php",
            u"%", u"%=", u"%@", u"%--", u"%!",
            u"!--", "!doctype"
        ]


    # --- setToSkip
    def setToSkip(self, toSkipNames):
        """Sets the elements which contents shall not be changed.

        If the given names of elements are None or empty, the default elements
        to skip are used.

        Otherwise, a list with the elements to skip is built.

        Args:
            toSkipNames (List[str]): The names of elements which shall not be changed

        Todo:
            Warn user if a non-XML-character occurs?
        """
        if toSkipNames is None or len(toSkipNames)==0:
            return
        self._elementsToSkip = [x.strip() for x in toSkipNames.split(',')]


    # --- setFormat
    def setFormat(self, formatS):
        """Sets the target character representation
        
        Args:
            formatS (str): The format to use, one of "html", "unicode", "text"
        """
        if formatS=="html":
            self._replFunc = _replFunc_HTML
        elif formatS=="unicode":
            self._replFunc = _replFunc_KEEP
        elif formatS=="text":
            self._replFunc = _replFunc_UNICODE
        else:
            raise ValueError("Unknown target format '%s'" % formatS)


    # --- _getTagName
    def _getTagName(self, html):
        """Returns the name of the tag that starts at the begin of the given string.

        Args:
            html (str): The HTML-subpart

        Returns:
            (str): The name of the tag
        """
        i = 0
        while i<len(html) and (ord(html[i])<=32 or html[i]=="/"):
            i = i + 1
        ib = i
        ie = i
        while ie<len(html) and html[ie] not in " \n\r\t>/":
            ie += 1
        return html[ib:ie]


    # --- _mark
    def _markHTML(self, html):
        """Returns a string where all HTML-elements are denoted as '1' and
        plain content as '0'.

        Args:
            html (str): The HTML document (contents) to process

        Returns:
            (str): Annotation of the HTML document.
        """
        # mark HTML elements
        html = html.lower()
        ret = ""
        i = 0
        while i<len(html):
            if html[i]=='<':
                ret = ret + "1"
            elif html[i]=='>':
                ret = ret + "1"
                i += 1
                continue
            else:
                ret = ret + "0"
                i += 1
                continue
            # process elements to skip contents of
            i += 1
            tb = self._getTagName(html[i:])
            ret += "1"*(len(tb))
            i = i + len(tb)
            if tb not in self._elementsToSkip:
                ie = html.find(">", i)
                if ie<0:
                    raise ValueError("Unclosed element at %s" % (i-len(tb)))
                ret += "1"*(ie-i+1)
                i = ie + 1
                continue
            ib = i
            if tb=="?" or tb=="?php":
                # assumption: php stuff is always closed by ?>
                ie = html.find("?>", ib)
                if ie<0: raise ValueError("Unclosed '<%s' element at position %s." % (tb, i))
                ie += 1
            elif tb=="%" or tb=="%=" or tb=="%@" or tb=="%--" or tb=="%!":
                # assumption: jsp/asp stuff is always closed by %>
                ie = html.find("%>", ib)
                if ie<0: raise ValueError("Unclosed '<%s' element at position %s." % (tb, i))
                ie += 1
            elif tb=="!--":
                # comments are always closed by -->
                ie = html.find("-->", ib)
                if ie<0: raise ValueError("Unclosed '<%s' element at position %s." % (tb, i))
                ie += 2
            elif tb=="!doctype":
                # DOCTYPE: find matching >
                ie = ib+1
                num = 1
                while ie<len(html):
                    if html[ie]=="<": num = num + 1
                    elif html[ie]==">": num = num + 1
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
                    ie1 = html.find("</"+tb, ie)
                    ie2 = html.find("<"+tb, ie)
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
        assert (len(ret)==len(html))
        return ret


    def _markMarkdown(self, document):
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

    # --- prettify
    def prettify(self, document, isHTML, isMarkdown=False):
        """Prettifies (degrotesques) the given document.

        It is assumed that the input is given in utf-8.

        The result is returned in utf-8 as well.

        Args:
            document (str): The document (contents) to process.
            isHTML (bool): Whether the document is a HTML document
            isMarkdown (bool): Whether the document is a markdown document

        Returns:
            (str): The processed (prettified / degrotesqued) document.
        """
        # extract text parts
        if isHTML:
            marks = self._markHTML(document)
        elif isMarkdown:
            marks = self._markMarkdown(document)
        else:
            marks = "0" * len(document)
        assert(len(document)==len(marks))
        # build a copy of actions to use (not found will be removed from it)
        actions = list(self._actions)
        for a in actions:
            # add placeholder for opening / closing regexp
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
                dest = self._targetRegex.sub(self._replFunc, a[1][1])
                tmp = a[0][1].sub(dest, document[epos:], 1)
                repLength = closing.end() - closing.start() + len(tmp) - len(document[epos:])
                document = document[:epos] + tmp
                marks = marks[:epos+closing.start()] + "1"*repLength + marks[epos+closing.end():]
                assert (len(document)==len(marks))
            opening = a[0][0].match(document[bpos:])
            dest = self._targetRegex.sub(self._replFunc, a[1][0])
            tmp = a[0][0].sub(dest, document[bpos:], 1)
            repLength = opening.end() + len(tmp) - len(document[bpos:])
            document = document[:bpos] + tmp
            marks = marks[:bpos] + "1"*repLength + marks[bpos+opening.end():]
            assert (len(document)==len(marks))
            # move in document, adapt actions list (found only)
            pos = bpos + opening.end() + 1
            actions = nactions
        return document




# --- functions -----------------------------------------------------
# --- getExtensions
def getExtensions(extNames):
    """Returns the list of extensions of files to process.

    If the given names of extensions are None or empty, the default
    extensions are used.

    Otherwise, the given string is split and returned as a list.

    Args:
        extNames (List[str]): The names of extensions to process (or None if default extensions shall be used)

    Returns:
        (List[str]): The list of extensions to use.

    todo:
        What about removing dots?
    """
    if extNames is None or len(extNames)==0:
        return None
    exts = [x.strip() for x in extNames.split(',')]
    if "*" in exts:
        return None
    return exts


# --- getFiles
def getFiles(name, recursive, extensions):
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
        raise ValueError("Can not process '%s'" % name) # pragma: no cover
    files.sort()
    files.sort(key=lambda v: str(v).replace("\\", "/").count('/'))
    return files


# --- main
def main(arguments=None):
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

    --format / -f _&lt;FORMAT&gt;_:
        Define the format of the replacements ['html', 'unicode', 'text']

    --no-backup / -B:
        Set if no backup files shall be generated

    --skip / -s _&lt;ELEMENT_NAME&gt;[,&lt;ELEMENT_NAME&gt;]\*_:
        Elements which contents shall not be changed

    --actions / -a _&lt;ACTION_NAME&gt;[,&lt;ACTION_NAME&gt;]\*_:
        Name the actions that shall be applied

    --help / -h:
        Prints the help screen

    --version / -v:
        Prints the version

    """
    sys.tracebacklimit = 0
    # parse options
    optParser = OptionParser(usage="\n  degrotesque.py [options]", version="degrotesque 3.0.0")
    optParser.add_option("-i", "--input", dest="input", default=None, help="Defines files/folder to process")
    optParser.add_option("-r", "--recursive", dest="recursive", action="store_true", default=False, help="Whether a given path shall be processed recursively")
    optParser.add_option("-e", "--extensions", dest="extensions", default=None, help="Defines the extensions of files to process")
    optParser.add_option("-E", "--encoding", dest="encoding", default="utf-8", help="File encoding (default: 'utf-8')")
    optParser.add_option("-H", "--html", dest="html", action="store_true", default=False, help="Files are HTML/XML-derivatives")
    optParser.add_option("-T", "--text", dest="text", action="store_true", default=False, help="Files are plain text files")
    optParser.add_option("-M", "--markdown", dest="markdown", action="store_true", default=False, help="Files are markdown files")
    optParser.add_option("-B", "--no-backup", dest="no_backup", action="store_true", default=False, help="Whether no backup shall be generated")
    optParser.add_option("-f", "--format", dest="format", default="unicode", help="Defines the format of the replacements ['html', 'unicode', 'text']")
    optParser.add_option("-s", "--skip", dest="skip", default=None, help="Defines the elements which contents shall not be changed")
    optParser.add_option("-a", "--actions", dest="actions", default=None, help="Defines the actions to perform")
    options, remaining_args = optParser.parse_args(args=arguments)
    # check options
    if options.input is None:
        print("Error: no input file(s) given...", file=sys.stderr)
        print("Usage: degrotesque.py -i <FILE>[,<FILE>]* [options]+", file=sys.stderr)
        sys.exit(2)
    # setup degrotesque
    degrotesque = Degrotesque()
    try:
        degrotesque.setActions(options.actions)
        degrotesque.setToSkip(options.skip)
        degrotesque.setFormat(options.format)
    except ValueError as err:
        print(str(err))
        sys.exit(3)
    # collect files
    extensions = getExtensions(options.extensions)
    files = getFiles(options.input, options.recursive, extensions)
    # the HTML recognition regexp
    # https://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags/1732454
    htmlRegex = re.compile("<(?:\"[^\"]*\"['\"]*|'[^']*'['\"]*|[^'\">])+>")
    # loop through files
    for f in files:
        print("Processing %s" % f)
        try:
            # read the file
            with io.open(f, mode="r", encoding=options.encoding) as fd:
                document = fd.read()
            # determine file contents (html/text)
            n, e = os.path.splitext(f)
            isHTML = options.html
            if not options.text and not options.markdown and not options.html:
                isHTML = e[1:] in htmlExtensions or htmlRegex.search(document) is not None
            isMarkdown = not options.html and not options.text and (options.markdown or e[1:] in markdownExtensions)
            # apply the beautifications
            document = degrotesque.prettify(document, isHTML, isMarkdown)
            # build a backup
            if not options.no_backup:
                shutil.copy(f, f+".orig")
            # save the new contents
            with io.open(f, mode="w", encoding=options.encoding) as fd:
                fd.write(document)
        except ValueError as err:
            print(str(err))
            sys.exit(4)


# -- main check
if __name__ == '__main__':
    main(sys.argv) # pragma: no cover
