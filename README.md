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

There are some caveats, yes. If you embed HTML code in HTML (not suported by HTML, but who cares), it may yield in odd behaviour.
If you have php-pages and combine php-generated and plain HTML text, it may yield in odd behaviour. Etc. So you should check your pages for correctness after applying degrotesque.

Currently, the following actions are supported:

| Action Name | From Opening String | From Closing String | To Opening String | To Closing String |
| ---- | ---- | ---- | ---- | ---- |
| quotes.english | " '" | "'" | " &lsquo;" | "&rsquo;" |
| | "\"" | "\"" | "&ldquo;" | "&rdquo;" |
| quotes.french | "&lt;" | "&gt;" | "&lsaquo;" | "&rsaquo;" |
| | "&lt;&lt;" | "&gt;&gt;" | "&laquo;" | "&raquo;" |
| quotes.german | " '" | "'" | " &sbquo;" | "&rsquo;" |
| | "\"" | "\"" | "&bdquo;" | "&rdquo;" |
| to_quotes | " '" | "'" | " <q>" | "</q>" |
| | "\"" | "\"" | "<q>" | "</q>" |
| | "&lt;&lt;" | "&gt;&gt;" | "<q>" | "</q>" |
| commercial | "(c)" | | "&copy;" | |
| | "(C)" | | "&copy;" | |
| | "(r)" | | "&reg;" | |
| | "(R)" | | "&reg;" | |
| | "(tm)" | | "&trade;" | |
| | "(TM)" | | "&trade;" | |
| dashes | " - " | | "&mdash;" | |
| bullets | "*" | | "&bull;" | |
| ellipsis | "..." | | "&hellip;" | |
| apostroph | "'" | | "&apos;" | |
| math | "+/-" | | "&plusmn;" | |
| | "1/2" | | "&frac12;" | |
| | "1/4" | | "&frac14;" | |
| | "~" | | "&asymp;" | |
| | "!=" | | "&ne;" | |
| | "<=" | | "&le;" | |
| | ">=" | | "&ge;" | |
| dagger | "*" | | "&dagger;" | |
| | "**" | | "&Dagger;" | |
 
