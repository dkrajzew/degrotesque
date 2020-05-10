from __future__ import print_function
"""degrotesque.py

A tiny web type setter.

The following options must be set

:param --input/-i: the file or the folder to process

The following options are optional

:param --recursive/-r: Set if the folder - if given - shall be processed recursively
:param --no-backup/-B: Set if no backup files shall be generated
:param --actions/-a: Name the actions that shall be applied
:param --extensions/-e: The extensions of files that shall be processed
:param --encoding/-f: File encoding (default: 'utf-8'")

The application reads the given file or the files from the folder (optionally 
recursive) defined by the -i/--input option that match either the default or
the extensions given using the -e/--extension option, applies the default
or the actions named using the -a/--actions option to the contents and
save the files under their original name. If the option -B/--no-backup is not
given, a backup of the original files is generated named as the original
file with the appendix ".orig".

(c) Daniel Krajzewicz 2020
daniel@krajzewicz.de
http://www.krajzewicz.de
http://www.krajzewicz.de/blog/degrotesque.php

Available under GPL 3.0, all rights reserved
"""


# --- imports -------------------------------------------------------
import sys, glob, os, io, shutil, re
from optparse import OptionParser


# --- variables and constants ---------------------------------------
"""A database of actions
Each action consists of
:param [0]: The string to match / the opening string to match
:param [1]: The closing string to match
:param [0]: The string to match
:param [0]: The string to match
"""
actionsDB = {
 # english quotes
 "quotes.english": [
   [[r" '", r"'"], [u" &lsquo;", u"&rsquo;"]],
   [[r"\"", r"\""], [u"&ldquo;", u"&rdquo;"]],
  ],

 # french quotes
 "quotes.french": [
   [[r"&lt;", r"&gt;"], [u"&lsaquo;", u"&rsaquo;"]], # !!! does nothing, I did not found the right replacement, yet
   [[r"&lt;&lt;", r"&gt;&gt;"], [u"&laquo;", u"&raquo;"]],
  ],
  
 # german quotes
 "quotes.german": [
   [[r" '", r"'"], [u" &sbquo;", u"&rsquo;"]],
   [[r"\"", r"\""], [u"&bdquo;", u"&rdquo;"]],
  ],
  
 # conversion to HTML quotes (<q>)
 "to_quotes": [
   [[r" '", r"'"], [u" <q>", u"</q>"]],
   [[r"\"", r"\""], [u"<q>", u"</q>"]],
   [[r"&lt;&lt;", r"&gt;&gt;"], [u"<q>", u"</q>"]],
  ],
  
 # commercial signs
 "commercial": [
   [[r"\(c\)", None], [u"&copy;", None]],
   [[r"\(C\)", None], [u"&copy;", None]],
   [[r"\(r\)", None], [u"&reg;", None]],
   [[r"\(R\)", None], [u"&reg;", None]],
   [[r"\(tm\)", None], [u"&trade;", None]],
   [[r"\(TM\)", None], [u"&trade;", None]],
  ],
  
 # dashes
 "dashes": [
   # missing: ndash for number ranges 
   [[r" - ", None], [u" &mdash; ", None]],
  ],

 # bullets
 "bullets": [
   [[r"\*", None], [u"&bull;", None]],
  ],
    
 # ellipsis
 "ellipsis": [
   [[r"\.\.\.", None], [u"&hellip;", None]],
  ],
    
 # apostrophe
 "apostrophe": [
   [[r"'", None], [u"&apos;", None]],
  ],
    
 # math signs
 "math": [
   # [[""], ["", "&deg;", ""]],
   [[r"\+/-", None], [u"&plusmn;", None]],
   [[r"1/2", None], [u"&frac12;", None]],
   [[r"1/4", None], [u"&frac14;", None]],
   [[r"\~", None], [u"&asymp;", None]],
   [[r"\!=", None], [u"&ne;", None]],
   [[r"<=", None], [u"&le;", None]],
   [[r">=", None], [u"&ge;", None]],
  ],
    
 # dagger
 "dagger": [
   [[r"\*\*", None], [u"&Dagger;", None]],
   [[r"\*", None], [u"&dagger;", None]],
  ]    
}


"""A database of extensions of files to process"""
extensionsDB = [ 
  "html", "htm", "xhtml",
  "php", "phtml", "phtm", "php2", "php3", "php4", "php5",
  "asp", 
  "jsp", "jspx", 
  "shtml", "shtm", "sht", "stm",
  "vbhtml",
  "ppthtml",   
  "ssp", "jhtml" ]

"""List of elements which coontents shall not be processed"""
elementsToSkip = [
 u"script", u"code", u"style", u"pre", u"?", u"?php"
]



# --- methods -------------------------------------------------------
# -- degrotesquing
def getTagName(html):
  i = 0
  while i<len(html) and ord(html[i])<=32:
    i = i + 1 
  if html[i]=="/":
    i = i + 1
  ib = i
  ie = i
  while ie<len(html) and html[ie] not in " \n\r\t>/":
    ie += 1 
  return html[ib:ie]      
   


def mark(html):
  opened = 0
  # mark HTML elements, first
  ret = ""
  for i in range(0, len(html)):
    if opened==0:
      ret = ret + "0"
    else:
      ret = ret + "1"
    if html[i]=='<':
      opened += 1   
      ret = ret[:-1] + "1"
    if html[i]=='>':
      opened -= 1
  # mark code parts
  i = 0
  while i<len(html):
    if html[i]=='<':
      tb = getTagName(html[i+1:])
      if tb not in elementsToSkip:
        i = i + len(tb)
        continue
      if tb=="?" or tb=="?php":
        ib = i
        ie = html.index("?>", ib)
      else:
        ie = -1
        i = html.find(">", i)
        ib = i
        while i<len(html) and ib<=i:
          n = html.find("/"+tb, i)
          if n<0:
            print ("unclosed element")
            print (tb)
            exit()
          if n<ib:
            print ("false")
            break
          te = getTagName(html[n:])
          if tb==te:
            ie = html.index(">", n+len(te))
            break
          print ("Nope")
      assert(len(ret)==len(html))
      if ib>=0 and ie>=0:
        ret = ret[:ib] + "1"*(ie-ib) + ret[ie:]
      assert(len(ret)==len(html))
      i = ie - 1
    i = i + 1
    assert(len(ret)==len(html))
  return ret      


def prettify(html, actions):
  """Prettifies (degrotesques) the given HTML snipplet using the given actions.
  
  It is assumed that the input is given in utf-8.
  The result is returned in utf-8 as well.
  """
  i = 0
  # extract text parts
  marks = mark(html)
  assert(len(html)==len(marks))
  while i<len(html):
    if marks[i]=="1":
      i = i + 1
      continue
    for a in actions:
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
        html = html[:ib] + re.sub(a[0][1], a[1][1], html[ib:], 1)
        marks = marks[:ib+closing.start()] + "0"*len(a[1][1]) + marks[ib+closing.end():]
        assert(len(html)==len(marks))
      html = html[:i] + re.sub(a[0][0], a[1][0], html[i:], 1)
      marks = marks[:i] + "0"*len(a[1][0]) + marks[i+opening.end():]
      assert(len(html)==len(marks))
      break
    i = i + 1
  return html
  


# -- options parsing
def getExtensions(extNames):
  """Returns the file extensions of files to process by evaluating the given options."""
  if extNames==None or len(extNames)==0:
    return extensionsDB
  return extNames.split(",")


def getActions(actNames):
  """Returns the actions to apply by evaluating the given options."""
  actions = []
  if actNames==None or len(actNames)==0:
    actions.extend(actionsDB["quotes.english"])
    actions.extend(actionsDB["dashes"])
    actions.extend(actionsDB["ellipsis"])
    actions.extend(actionsDB["math"])
    actions.extend(actionsDB["apostrophe"])
    return actions
  actNames = actNames.split(",")
  for an in actNames:
    if an in actionsDB:
      actions.extend(actionsDB[an])
    else:
      raise ValueError("Action '%s' is not known." % (an))
  return actions


def getFiles(name, recursive, extensions):
  """Returns the files to process."""
  files = []
  if os.path.isdir(name):  
    for root, dirs, dfiles in os.walk(name):
      for f in dfiles:
        n, e = os.path.splitext(os.path.join(root, f))
        e = e[1:]
        if e not in extensions:
          continue
        files.append(os.path.join(root, f))
      if not recursive:
        break
  elif os.path.isfile(name):  
    files.append(name)  
  else:  
    raise ValueError("Can not process '%s'" % name)
  return files



# -- main
def main(call):
  """Parses the options, first. Determines the extenions of files to consider, 
  the files to process, and the actions to apply. Goes through the list of 
  files and prettyfies (degrotesques) them. 
  """
  optParser = OptionParser(usage="usage:\n  %prog [options]", version="%prog 0.6")
  optParser.add_option("-i", "--input", dest="input", default=None, help="Defines files/folder to process")
  optParser.add_option("-f", "--encoding", dest="encoding", default="utf-8", help="File encoding (default: 'utf-8'")
  optParser.add_option("-r", "--recursive", dest="recursive", action="store_true", default=False, help="Whether a given path shall be processed recursively")
  optParser.add_option("-B", "--no-backup", dest="no_backup", action="store_true", default=False, help="Whether no backup shall be generated")
  optParser.add_option("-e", "--extensions", dest="extensions", default=None, help="Defines the extensions of files to process")
  optParser.add_option("-a", "--actions", dest="actions", default=None, help="Defines the actions to perform")
  options, remaining_args = optParser.parse_args(args=call)
  extensions = getExtensions(options.extensions)
  actions = getActions(options.actions)
  if options.input==None:
    optParser.error("no input file(s) given...")
    sys.exit()
  files = getFiles(options.input, options.recursive, extensions)
  for f in files:
    print("Processing %s" % f)
    try:
      # read the file
      fd = io.open(f, mode="r", encoding=options.encoding)
      html = fd.read()
      fd.close()
      html = html.encode("utf-8", "ignore")
      # apply the beautifications
      html = prettify(html, actions)
      # save it
      html = html.decode(options.encoding)
      if not options.no_backup:
        shutil.copy(f, f+".orig")
      fd = io.open(f, mode="w", encoding=options.encoding)
      fd.write(html)
      fd.close()
    except ValueError as err:
      print(str(err))
      continue



# -- main check
if __name__ == '__main__':
  main(sys.argv)
    
    

