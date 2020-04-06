"""degrotesque.py

A tiny web type setter.

The following options must be set

:param --input/-i: the file or the folder to process

The following options are optional

:param --recursive/-r: Set if the folder - if given - shall be processed recursively
:param --no-backup/-B: Set if no backup files shall be generated
:param --actions/-a: Name the actions that shall be applied
:param --extensions/-e: The extensions of files that shall be processed

The application reads the given file or the files from the folder (optionally 
recursive) defined by the -i/--input option that match either the default or
the extensions given using the -e/--extension option, applies the default
or the actions named using the -a/--actions option to the contents and
save the files under their original name. If the option -B/--no-backup is not
given, a backup of the original files is generated named as the original
file with the appendix ".orig".

(c) Daniel Krajzewicz 2020
daniel@krajzewicz.de

Available under GPL 3.0, all rights reserved
"""


# --- imports -------------------------------------------------------
import sys
import glob
import os  
import shutil
from optparse import OptionParser


# --- variables and constants ---------------------------------------
"""A database of actions"""
actionsDB = {
 # english quotes
 "quotes.english": [
   # [0]: matching end, [1]: replacement at begin, [2]: replacement at end
   [[" '"], ["'", " &lsquo;", "&rsquo;"]],
   [["\""], ["\"", "&ldquo;", "&rdquo;"]],
  ],

 # french quotes
 "quotes.french": [
   [["&lt;"], ["&gt;", "&lsaquo;", "&rsaquo;"]], # !!! does nothing, I did not found the right replacement, yet
   [["&lt;&lt;"], ["&gt;&gt;", "&laquo;", "&raquo;"]],
  ],
  
 # german quotes
 "quotes.german": [
   [[" '"], ["'", " &sbquo;", "&rsquo;"]],
   [["\""], ["\"", "&bdquo;", "&rdquo;"]],
  ],
  
 # conversion to HTML quotes (<q>)
 "to_quotes": [
   [[" '"], ["'", " <q>", "</q>"]],
   [["\""], ["\"", "<q>", "</q>"]],
   [["&lt;&lt;"], ["&gt;&gt;", "<q>", "</q>"]],
  ],
  
 # commercial signs
 "commercial": [
   [["(c)"], ["", "&copy;", ""]],
   [["(C)"], ["", "&copy;", ""]],
   [["(r)"], ["", "&reg;", ""]],
   [["(R)"], ["", "&reg;", ""]],
   [["(tm)"], ["", "&trade;", ""]],
   [["(TM)"], ["", "&trade;", ""]],
  ],
  
 # dashes
 "dashes": [
   # missing: ndash for number ranges 
   [[" - "], ["", " &mdash; ", ""]],
  ],

 # bullets
 "bullets": [
   [["*"], ["", "&bull;", ""]],
  ],
    
 # ellipsis
 "ellipsis": [
   [["..."], ["", "&hellip;", ""]],
  ],
    
 # apostroph
 "apostroph": [
   [["'"], ["", "&apos;", ""]],
  ],
    
 # math signs
 "math": [
   # [[""], ["", "&deg;", ""]],
   [["+/-"], ["", "&plusmn;", ""]],
   [["1/2"], ["", "&frac12;", ""]],
   [["1/4"], ["", "&frac14;", ""]],
   [["~"], ["", "&asymp;", ""]],
   [["!="], ["", "&ne;", ""]],
   [["<="], ["", "&le;", ""]],
   [[">="], ["", "&ge;", ""]],
  ],
    
 # dagger
 "dagger": [
   [["*"], ["", "&dagger;", ""]],
   [["**"], ["", "&Dagger;", ""]],
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
  while i<len(html) and html[i]!='>':
    i = i + 1
  return i + 1, False
   


def prettify(html, actions, log=[]): # empty, dismissed log if nothing's passed as reference
  """Prettifies (degrotesques) the given HTML snipplet using the given actions."""
  i = 0
  opened = False
  findEnd = None
  while i<len(html): # iterate over the document
    if opened:
      if html[i]=='>':
        opened = False
      i = i + 1
      continue
    if html[i]=='<':
      i, opened = skipIfCode(html, i)
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
    #actions.extend(actionsDB["dagger"])
    actions.extend(actionsDB["apostroph"])
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
  optParser = OptionParser(usage="""usage:\n  %prog [options]""")
  optParser.add_option("-i", "--input", dest="input", default=None, help="Defines files/folder to process")
  optParser.add_option("-r", "--recursive", dest="recursive", action="store_true", default=False, help="Whether a given path shall be processed recursively")
  optParser.add_option("-B", "--no-backup", dest="no_backup", action="store_true", default=False, help="Whether no backup shall be generated")
  optParser.add_option("-e", "--extensions", dest="extensions", default=None, help="Defines the extensions to process")
  optParser.add_option("-a", "--actions", dest="actions", default=None, help="Defines the actions to perform")
  options, remaining_args = optParser.parse_args(args=call)
  extensions = getExtensions(options.extensions)
  actions = getActions(options.actions)
  files = getFiles(options.input, options.recursive, extensions)
  for f in files:
    print "Processing %s" % f
    try:
      with open(f, 'r') as file:
        html = file.read()
      html = prettify(html, actions)
      if not options.no_backup:
        shutil.copy(f, f+".orig")
      with open(f, 'w') as file:
        file.write(html)
    except ValueError as err:
      print str(err)
      continue



# -- main check
if __name__ == '__main__':
  main(sys.argv)
    
    

