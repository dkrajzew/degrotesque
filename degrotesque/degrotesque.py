from __future__ import print_function
"""degrotesque.py

A tiny web type setter.
Version 1.6

(c) Daniel Krajzewicz 2020-2022
daniel@krajzewicz.de
http://www.krajzewicz.de
https://github.com/dkrajzew/degrotesque
http://www.krajzewicz.de/blog/degrotesque.php

Available under LGPL 3 or later, all rights reserved
"""


# --- imports -------------------------------------------------------
import sys, glob, os, io, shutil, re
from optparse import OptionParser
from html.parser import HTMLParser



# --- variables and constants ---------------------------------------
"""A database of actions"""
actionsDB = {
 # english quotes
 "quotes.english": [
   [[u"(\\s+)'", u"'"],             [u"\\1&lsquo;", u"&rsquo;"],    [u"\\1&#8216;", u"&#8217;"]],
   [[u"\"", u"\""],                 [u"&ldquo;", u"&rdquo;"],       [u"&#8220;", u"&#8221;"]]
  ],

 # french quotes
 "quotes.french": [
   [[u"&lt;&lt;", u"&gt;&gt;"],     [u"&laquo;", u"&raquo;"],       [u"&#x00AB;", u"&#x00BB;"]],
   [[u"&lt;", u"&gt;"],             [u"&lsaquo;", u"&rsaquo;"],     [u"&#x2039;", u"&#x203A;"]]
  ],
  
 # german quotes
 "quotes.german": [
   [[u"(\\s+)'", u"'"],             [u"\\1&sbquo;", u"&rsquo;"],    [u"\\1&#x201A;", u"&#x2019;"]],
   [[u"\"", u"\""],                 [u"&bdquo;", u"&rdquo;"],       [u"&#x201E;", u"&#x201D;"]]
  ],
  
 # conversion to HTML quotes (<q>)
 "to_quotes": [
   [[u"(\\s+)'", u"'"],             [u"\\1<q>", u"</q>"],           [u"\\1<q>", u"</q>"]],
   [[u"\"", u"\""],                 [u"<q>", u"</q>"],              [u"<q>", u"</q>"]],
   [[u"&lt;&lt;", u"&gt;&gt;"],     [u"<q>", u"</q>"],              [u"<q>", u"</q>"]],
   [[u"&lt;", u"&gt;"],             [u"<q>", u"</q>"],              [u"<q>", u"</q>"]]
  ],
  
 # commercial signs
 "commercial": [
   [[u"\\([c|C]\\)", None],         [u"&copy;", None],              [u"&#169;", None]],
   [[u"\\([r|R]\\)", None],         [u"&reg;", None],               [u"&#174;", None]],
   [[u"\\([t|T][m|M]\\)", None],    [u"&trade;", None],             [u"&#8482;", None]]
  ],
  
 # dashes
 "dashes": [
   # missing: ndash for number ranges 
   [[u"(\\s+)-(\\s+)", None],       [u"\\1&mdash;\\2", None],       [u"\\1&#8212;\\2", None]],
   [[u"([\\d]+)-([\\d]+)", None],   [u"\\1&ndash;\\2", None],       [u"\\1&#8211;\\2", None]]
  ],

 # bullets
 "bullets": [
   [[u"\\*", None],                 [u"&bull;", None],              [u"&#8226;", None]]
  ],
    
 # ellipsis
 "ellipsis": [
   [[u"\\.\\.\\.", None],           [u"&hellip;", None],            [u"&#8230;", None]]
  ],
    
 # apostrophe
 "apostrophe": [
   [[u"'", None],                   [u"&apos;", None],              [u"&#39;", None]]
  ],
    
 # dagger
 "dagger": [
   [[u"\\*\\*", None],              [u"&Dagger;", None],            [u"&#8225;", None]],
   [[u"\\*", None],                 [u"&dagger;", None],            [u"&#8224;", None]]
  ],    

 # math signs
 "math": [
   [[u"\\+/-", None],               [u"&plusmn;", None],            [u"&#177;", None]],
   [[u"1/2", None],                 [u"&frac12;", None],            [u"&#189;", None]],
   [[u"1/4", None],                 [u"&frac14;", None],            [u"&#188;", None]],
   [[u"3/4", None],                 [u"&frac34;", None],            [u"&#190;", None]],
   [[u"\\~", None],                 [u"&asymp;", None],             [u"&#8776;", None]],
   [[u"\\!=", None],                [u"&ne;", None],                [u"&#8800;", None]],
   [[u"&lt;=", None],               [u"&le;", None],                [u"&#8804;", None]],
   [[u"&gt;=", None],               [u"&ge;", None],                [u"&#8805;", None]],
   [[u"([\\d]+)(\\s*)\*(\\s*)([\\d]+)", None],  [u"\\1\\2&times;\\3\\4", None],     [u"\\1\\2&#215;\\3\\4", None]],
   [[u"([\\d]+)(\\s*)x(\\s*)([\\d]+)", None],   [u"\\1\\2&times;\\3\\4", None],     [u"\\1\\2&#215;\\3\\4", None]],
   [[u"([\\d]+)(\\s*)/(\\s*)([\\d]+)", None],   [u"\\1\\2&divide;\\3\\4", None],    [u"\\1\\2&#247;\\3\\4", None]]
  ],
    
 # chem
 "chem": [
   [[u"([a-zA-Z]+)([\\d]+)", None],        [u"\\1<sub>\\2</sub>", None],   [u"\\1<sub>\\2</sub>", None]]
  ],
    
 # masks
 "masks": [
   [[u"978-([\\d]+)-([\\d]+)-([\\d]+)-([\\d])(\\D)", None], [u"978-\\1-\\2-\\3-\\4\\5", None],  [u"978-\\1-\\2-\\3-\\4\\5", None]],
   [[u"979-([\\d]+)-([\\d]+)-([\\d]+)-([\\d])(\\D)", None], [u"979-\\1-\\2-\\3-\\4\\5", None],  [u"979-\\1-\\2-\\3-\\4\\5", None]],
   [[u"([\\d]+)-([\\d]+)-([\\d]+)-([\\d])(\\D)", None],     [u"\\1-\\2-\\3-\\4\\5", None],      [u"\\1-\\2-\\3-\\4\\5", None]],
   [[u"ISSN (\\d{4})-(\\d{4})(\\D)", None],                 [u"ISSN \\1-\\2\\3", None],         [u"ISSN \\1-\\2\\3", None]]
  ]    
}


"""A database of extensions of files to process"""
extensionsDB = [
  "html", "htm", "xhtml",
  "php", "phtml", "phtm", "php2", "php3", "php4", "php5",
  "asp",
  "jsp", "jspx",
  "shtml", "shtm", "sht", "stm",
  "vbhtml", "ppthtml", "ssp", "jhtml"
]



# --- class ---------------------------------------------------------
class Degrotesque():
  """The tiny web type setter.
     The main method "prettify" uses the list of actions to change the contents
     of the given HTML page.
     Elements are skipped as well as the contents of some specific elements.
     Additional method support parsing and setting of new values for actions
     and elements to skip.
     Some internal methods exist for determining which parts of the document 
     shall processed and which ones are to skip."""
     
  # --- init
  def __init__(self):
    """Sets defaults for the elements which contents shall not be processed.
       Sets defaults for actions to perform."""
    # the elements to skip
    self._restoreDefaultElementsToSkip()
    # the actions to apply
    self._restoreDefaultActions()
     
     
  # --- restoreDefaultActions
  def _restoreDefaultActions(self):
    """Instantiates default actions"""     
    self._actions = []
    self._actions.extend(actionsDB["masks"])
    self._actions.extend(actionsDB["quotes.english"])
    self._actions.extend(actionsDB["dashes"])
    self._actions.extend(actionsDB["ellipsis"])
    self._actions.extend(actionsDB["math"])
    self._actions.extend(actionsDB["apostrophe"])
  
    
  # --- setActions
  def setActions(self, actNames):
    """Returns the actions to apply.
       If the given names of actions are None or empty, the default actions 
       are used.
       Otherwise, the actions matching the given names are retrieved from the
       internal database and their list is returned.
       :param actNames The names of the actions to use (or None if default 
                       actions shall be used)"""
    if actNames==None or len(actNames)==0:
      return
    actNames = actNames.split(",")
    self._actions = []
    for an in actNames:
      if an in actionsDB:
        self._actions.extend(actionsDB[an])
      else:
        raise ValueError("Action '%s' is not known." % (an))


  # --- restoreDefaultActions
  def _restoreDefaultElementsToSkip(self):
    """Instantiates default elements to skip"""
    # list of elements which contents shall not be processed
    self._elementsToSkip = [
      u"script", u"code", u"style", u"pre", u"?", u"?php", 
      u"%", u"%=", u"%@", u"%--", u"%!",
      u"!--", "!DOCTYPE"
    ]


  # --- setToSkip
  def setToSkip(self, toSkipNames):
    """Returns the elements which contents shall not be changed.
       If the given names of elements are None or empty, the default elements 
       to skip are used.
       Otherwise, a list with the elements to skip is built.
       :param toSkipNames The names of elements which shall not be changed
       :todo Warn user if a non-XML-character occurs?
       """
    if toSkipNames==None or len(toSkipNames)==0:
      return 
    self._elementsToSkip = [x.strip() for x in toSkipNames.split(',')] 


  # --- _getTagName
  def _getTagName(self, html):
    """Returns the name of the tag that starts at the begin of the given string.
       :param html The HTML-subpart"""
    i = 0
    while i<len(html) and (ord(html[i])<=32 or html[i]=="/"):
      i = i + 1 
    ib = i
    ie = i
    while ie<len(html) and html[ie] not in " \n\r\t>/":
      ie += 1 
    return html[ib:ie]      


  # --- _mark
  def _mark(self, html):
    """Returns a string where all HTML-elements are denoted as '1' and plain text as '0'.
       :param html The html document (contents) to process"""
    # mark HTML elements, first
    ret = ""
    i = 0
    while i<len(html):
      opened = False
      if html[i]=='<':
        ret = ret + "1"
        opened = True
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
      elif tb=="!DOCTYPE":
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
            if ie1<0: raise ValueError("Unclosed '<%s' element at position %s." % (tb, i))
            ie = len(html)
            break
          if ie1>=0 and (ie1<ie2 or ie2<0):
            num = num - 1
            ie = ie1 + len("</"+tb)
          if ie2>=0 and (ie2<ie1 or ie1<0):
            num = num + 1
            ie = ie2 + len("<"+tb)
          if num==0: break
      ret += "1"*(ie-ib)
      i = ie
    assert(len(ret)==len(html))
    return ret      


  # --- prettify
  def prettify(self, html, useUnicode=False):
    """Prettifies (degrotesques) the given HTML snipplet using the given actions.
       It is assumed that the input is given in utf-8.
       The result is returned in utf-8 as well.
       :param html The html document (contents) to process
       :param actions The actions to apply"""
    i = 0
    # extract text parts
    lowerHTML = html.lower()
    marks = self._mark(lowerHTML)
    assert(len(html)==len(marks))
    while i<len(html):
      if marks[i]=="1":
        i = i + 1
        continue
      for a in self._actions:
        opening = re.match(a[0][0], html[i:])
        if not opening or marks[i+opening.start():i+opening.end()].find("1")>=0:
          continue 
        ib = i + opening.end()
        closing = None
        if a[0][1]!=None:
          while True:
            closing = re.search(a[0][1], html[ib:])
            if not closing:
              break
            if marks[ib+closing.start():ib+closing.end()].find("1")<0:
              break
            ib = ib + closing.end() 
            closing = None
        if a[0][1]!=None and closing==None:
          continue
        if closing!=None:
          if useUnicode: tmp = re.sub(a[0][1], a[2][1], html[ib:], 1)
          else: tmp = re.sub(a[0][1], a[1][1], html[ib:], 1)
          l = closing.end() - closing.start() + len(tmp) - len(html[ib:]) 
          html = html[:ib] + tmp
          marks = marks[:ib+closing.start()] + "1"*l + marks[ib+closing.end():]
          assert(len(html)==len(marks))
        if useUnicode: tmp = re.sub(a[0][0], a[2][0], html[i:], 1)
        else: tmp = re.sub(a[0][0], a[1][0], html[i:], 1)
        l = opening.end() + len(tmp) - len(html[i:])
        html = html[:i] + tmp
        marks = marks[:i] + "1"*l + marks[i+opening.end():]
        assert(len(html)==len(marks))
        i = i + l - 1
        break
      i = i + 1
    return html




# --- methods -------------------------------------------------------
# --- getExtensions 
def getExtensions(extNames):
  """Returns the list of extensions of files to process
     If the given names of extensions are None or empty, the default 
     extensions are used.
     Otherwise, the given string is split and returned as a list.
     :param extNames The names of extensions to process (or None if default 
                     extensions shall be used)
     :todo What about removing dots?"""
  if extNames==None or len(extNames)==0:
    return extensionsDB
  return [x.strip() for x in extNames.split(',')] 


# --- getFiles 
def getFiles(name, recursive, extensions):
  """Returns the files to process.
     If a file name is given, a list with only this filename is returned.
     If a folder name is given, the files to process are determined by walking
     throgh the folder - recursively if wished - and collecting all files
     that match the extensions. Returned is the list of collected files.   
     :param name The name of the file/folder
     :param recursive Whether the folder (if given) shall be processed recursively
     :param extensions The extensions of the files to process"""
  files = []
  if os.path.isdir(name):  
    for root, dirs, dfiles in os.walk(name):
      for f in dfiles:
        n, e = os.path.splitext(os.path.join(root, f))
        if e[1:] not in extensions:
          continue
        files.append(os.path.join(root, f))
      if not recursive:
        break
  elif os.path.isfile(name):  
    files.append(name)  
  else:  
    raise ValueError("Can not process '%s'" % name)
  return files


# --- main
def main(args):
  """The main method
  
  The following options must be set:

  :param --input/-i: the file or the folder to process

  The following options are optional:

  :param --recursive/-r: Set if the folder - if given - shall be processed recursively
  :param --no-backup/-B: Set if no backup files shall be generated
  :param --unicode/-u: Set if unicode values shall be used instead of HTML entities
  :param --extensions/-e: The extensions of files that shall be processed
  :param --encoding/-E: File encoding (default: 'utf-8'")
  :param --skip/-s: Elements which contents shall not be changed
  :param --actions/-a: Name the actions that shall be applied

  The application reads the given file or the files from the folder (optionally 
  recursive) defined by the -i/--input option that match either the default or
  the extensions given using the -e/--extension option, applies the default
  or the actions named using the -a/--actions option to the contents and
  save the files under their original name. If the option -B/--no-backup is not
  given, a backup of the original files is generated named as the original
  file with the appendix ".orig". When -u/--unicode is set, the replacement
  will use unicode numbers, otherwise HTML entities are used.
  """
  sys.tracebacklimit = 0
  # parse options
  optParser = OptionParser(usage="usage:\n  degrotesque.py [options]", version="degrotesque.py 1.6")
  optParser.add_option("-i", "--input", dest="input", default=None, help="Defines files/folder to process")
  optParser.add_option("-r", "--recursive", dest="recursive", action="store_true", default=False, help="Whether a given path shall be processed recursively")
  optParser.add_option("-B", "--no-backup", dest="no_backup", action="store_true", default=False, help="Whether no backup shall be generated")
  optParser.add_option("-u", "--unicode", dest="unicode", action="store_true", default=False, help="Use unicode characters instead of HTML entities")
  optParser.add_option("-e", "--extensions", dest="extensions", default=None, help="Defines the extensions of files to process")
  optParser.add_option("-E", "--encoding", dest="encoding", default="utf-8", help="File encoding (default: 'utf-8')")
  optParser.add_option("-s", "--skip", dest="skip", default=None, help="Defines the elements which contents shall not be changed")
  optParser.add_option("-a", "--actions", dest="actions", default=None, help="Defines the actions to perform")
  options, remaining_args = optParser.parse_args(args=args)
  # check options
  if options.input==None:
    print ("Error: no input file(s) given...", file=sys.stderr)
    print ("Usage: degrotesque.py -i <FILE>[,<FILE>]* [options]+", file=sys.stderr)
    sys.exit(2)
  # setup degrotesque
  degrotesque = Degrotesque()
  degrotesque.setActions(options.actions)
  degrotesque.setToSkip(options.skip)
  # collect files
  extensions = getExtensions(options.extensions)
  files = getFiles(options.input, options.recursive, extensions)
  # loop through files
  for f in files:
    print("Processing %s" % f)
    try:
      # read the file
      fd = io.open(f, mode="r", encoding=options.encoding)
      html = fd.read()
      fd.close()
      # apply the beautifications
      html = degrotesque.prettify(html, options.unicode)
      # build a backup
      if not options.no_backup:
        shutil.copy(f, f+".orig")
      # save the new contents
      fd = io.open(f, mode="w", encoding=options.encoding)
      fd.write(html)
      fd.close()
    except ValueError as err:
      print (str(err))
      continue


# -- main check
if __name__ == '__main__':
  main(sys.argv)
    
    

