%DKBUILD_DOCBOOK%\libxslt-1.1.26.win32\bin\xsltproc.exe --output man-degrotesque.html single_html.xsl man-degrotesque.xml
%DKBUILD_DOCBOOK%\libxslt-1.1.26.win32\bin\xsltproc.exe --output man-degrotesque.fo single_fo.xsl man-degrotesque.xml
call %DKBUILD_DOCBOOK%\fop-2.6\fop\fop man-degrotesque.fo -pdf man-degrotesque.pdf


