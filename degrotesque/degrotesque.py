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


# --- methods -------------------------------------------------------
# -- degrotesquing
def action_use(action, html, i):
  """Applies an action to the given HTML snipplet if the action matches.
  
  Returns the next index or -1 if the action could not be applied."""
  if html[i:i+len(action[0][0])]!=action[0][0]:
    return -1, html # does not match
  if len(action[1][0])==0:
    html = html[:i] + action[1][1] + html[i+len(action[0][0]):]
    return i - len(action[0][0]) + len(action[1][1]), html
  j = i + len(action[0][0])
  opened = False
  while j<len(html):
    if opened:
      if html[j]=='>':
        opened = False
      j = j + 1
      continue
    if html[j]=='<':
      opened = True
      j = j + 1
      continue
    if html[j:j+len(action[1][0])]!=action[1][0]:
      j = j + 1
      continue
    html = html[:j] + action[1][2] + html[j+len(action[1][0]):]
    html = html[:i] + action[1][1] + html[i+len(action[0][0]):]
    return i - len(action[0][0]) + len(action[1][1]), html
  return -1, html



def skipIfCode(html, i):
  """Skips a part of the HTML snipplet if it shall be not processed.
  
  This counts for script, style, and pre elements."""
  toFind = None
  i = i + 1
  if html[i:i+6].lower()=="script":
    toFind = "</script"       
    i = i + 6
  if html[i:i+4].lower()=="code":
    toFind = "</code"
    i = i + 4
  if html[i:i+5].lower()=="style":
    toFind = "</style"
    i = i + 5
  if html[i:i+3].lower()=="pre":
    toFind = "</pre"
    i = i + 3
  if html[i:i+1]=="?":
    toFind = "?>"
    i = i + 1
  if toFind==None:
    return i, True
  while i<len(html) and html[i:i+len(toFind)]!=toFind:
    i = i + 1
  if html[i:i+len(toFind)].lower()!=toFind:
    raise ValueError("Could not find matching end of '%s'" % toFind)
  if toFind!="?>":
    while i<len(html) and html[i]!='>':
      i = i + 1
  return i + 1, False
   


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
   

elementsToSkip = [
 u"script", u"code", u"style", u"pre", u"?", u"?php"
]


def mark(html):
  opened = 0
  #print (len(html))
  # mark first
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
    #print ("%s %s" % (i, len(html)))
    if html[i]=='<':
      #print (html[i-50:i+50])
      #if i==145:
      #print (html[i+1:i+50]) 
      tb = getTagName(html[i+1:])
      #print (len(tb))
      #print ("'" + tb + "' " + str(i))
      if tb not in elementsToSkip:
        i = i + len(tb)
        continue
      if tb=="?" or tb=="?php":
        #print("here")
        ib = i
        ie = html.index("?>", ib)
      else:
        ie = -1
        i = html.find(">", i)
        ib = i
        while i<len(html) and ib<=i:
          n = html.find("/"+tb, i)
          #print (tb + "  " + str(n) + "  " + str(i))
          if n<0:
            print ("unclosed element")
            print (tb)
            exit()
          if n<ib:
            print ("false")
            break
          #print (html[n-5:n+50])
          te = getTagName(html[n:])
          #print ("te: %s" % te)
          if tb==te:
            ie = html.index(">", n+len(te))
            #print ("ie: %s" % ie)
            break
          print ("Nope")
      #print ("a1 %s %s" % (ib, ie))
      assert(len(ret)==len(html))
      if ib>=0 and ie>=0:
        ret = ret[:ib] + "1"*(ie-ib) + ret[ie:]
      assert(len(ret)==len(html))
      i = ie - 1
      #print ("a2 %s %s %s" % (ib, ie, i))
      #print ("a2 %s" % (i))
    i = i + 1
    assert(len(ret)==len(html))
  return ret      
        
        
    
  
  

  
          
    

   

"""
def getTextAndIndices(html):
  retStr = ""
  retIdx = []
  opening = 0
  codeBlock = []
  i = 0
  while i<len(html):
    j = html.find("<", i)
    if j<0: j = len(html)
    print (j)
    if j!=i:
      retStr += html[i:j]
      retIdx.extend(range(i, j))
    opening = 1
    cb = None
    if html[i+1:].startswith("script"):
      cb = "script" 
    elif html[i+1:].startswith("code"):
      cb = "code" 
    elif html[i+1:].startswith("style"):
      cb = "style" 
    elif html[i+1:].startswith("pre"):
      cb = "pre" 
    elif html[i+1]=='?':
      cb = "?" 
    #print ("cb: %s" % cb)
    if cb!=None:
      if cb=='?':
        j = html.find("?>", j+len(cb))
        j = j + 2
      else:
        j = html.find("/"+cb+">", j+len(cb))
        j = j + len(cb) + 2
    else:
      j = j + 1
      #print ("Here %s %s %s" % (i, j, len(html)))
      while j<len(html):
        #print ("%s %s %s" % (j, html[j], opening))
        if html[j]=='<':
          opening = opening + 1
        elif html[j]=='>':
          opening = opening - 1
        j = j + 1
        if opening==0:
          break
      #print ("Here %s %s %s" % (i, j, len(html)))
      i = j
  print (retStr)
  return retStr, retIdx
"""

def prettify(html, marks, actions, log=[]): # empty, dismissed log if nothing's passed as reference
  """Prettifies (degrotesques) the given HTML snipplet using the given actions.
  
  It is assumed that the input is given in utf-8.
  The result is returned in utf-8 as well.
  """
  #print ("a1")
  #print (marks)
  i = 0
  assert(len(html)==len(marks))
  while i<len(html):
    #print ("%s %s" % (i, len(html)))
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
          closing = re.match(a[0][1], html[ib:])
          if not closing:
            break
          if marks[ib+closing.start():ib+closing.end()].find("1")<0:
            break
          ib = ib + closing.end() 
          closing = None
      if a[0][1]!=None and closing==None:
        continue
      #print (a)
      #print (opening.group(0))
      #print (opening.span(0))
      if closing!=None:
        html = html[:ib] + re.sub(a[0][1], a[1][1], html[ib:], 1)
        marks = marks[:ib+closing.begin()] + "0"*len(a[1][1]) + marks[ib+closing.end():]
        assert(len(html)==len(marks))
      html = html[:i] + re.sub(a[0][0], a[1][0], html[i:], 1)
      #print ("0"*len(a[1][0]))
      marks = marks[:i] + "0"*len(a[1][0]) + marks[i+opening.end():]
      #print (len(html))
      #print (len(marks))
      assert(len(html)==len(marks))
      break
    i = i + 1
  return html
  
  
"""  
  i = 0
  opened = False
  oN = 0
  findEnd = None
  while i<len(html): # iterate over the document
    if opened:
      if html[i]=='>':
        oN -= 1
      elif html[i]=='<':
        oN += 1
      if oN==0:
        opened = False
      i = i + 1
      continue
    if html[i]=='<':
      i, opened = skipIfCode(html, i)
      if opened:
        oN += 1
      continue
    found = False
    for a in actions:
      nextIndex, html = action_use(a, html, i)
      if nextIndex<0:
        continue
      found = True
      i = nextIndex
    if not found:
      i = i + 1
  return html      
"""


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
#  for ia,a in enumerate(actions):
#    if actions[ia][0][0]!=None: 
#      actions[ia][0][0] = re.compile(actions[ia][0][0])
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
      
      # extract text parts
      marks = mark(html)
      assert(len(html)==len(marks))
      #fdo = open("t2.txt", "w")
      #fdo.write(marks)
      #fdo.close()
      
      # apply the beautifications
      html = prettify(html, marks, actions)
      
      
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
    
    

