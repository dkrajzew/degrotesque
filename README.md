degrotesque - a tiny web type setter

The script loads a HTML page - or several in batch, one after the other - and for each, it replaces some commonly used non-typographic characters, such as ", ', -, etc. into their typograhic representant for improving the pages' appearance.  

E.g.:

 "Well - that's not what I had expected."

will become:

 &ldquo;Well &mdash; that&apos;s not what I had expected.&rdquo;

The script has the following options:
* --input/-i: the file or the folder to process
* --recursive/-r: Set if the folder - if given - shall be processed recursively
* --no-backup/-B: Set if no backup files shall be generated
* --actions/-a: Name the actions that shall be applied
* --extensions/-e: The extensions of files that shall be processed


 
