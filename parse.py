from __future__ import print_function
import sys
from HTMLParser import HTMLParser

for fi in sys.argv[1:]:
    if len(fi.split('.'))<2 or (fi.split('.')[1] != 'html' and fi.split('.')[1] !='htm'):
        exit(0)
    out = open(fi.split('.')[0]+'.parsed',"wb")
    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            return None
        def handle_endtag(self, tag):
            return None
        def handle_data(self, data):
            print(data,file=out)

    parser = MyHTMLParser()
    parser.feed(open(fi).read())
