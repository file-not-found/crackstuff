#!/usr/bin/env python2
from bs4 import BeautifulSoup
from urllib2 import Request,urlopen

outfile='webcrawl.out'
baseurl='http://exitno.de/'

nogo=('css','js','pdf')

def valid_link(ref):
    if not ref[0] == '/':
        return False
    elif ref.split('.')[-1] in nogo:
        return False
    else:
        return True

def get_words(url, handle, depth):
    req= Request(url)
    resp= urlopen(req)
    html= resp.read()

    soup=BeautifulSoup(html, 'html.parser')

    try:
        text=soup.body.text.encode('utf-8')
    except:
        text=None

    if text != None:
        for word in text.split():
            if handle != None:
                handle.write(word+"\n")
            else:
                print(word)

        if depth > 0:
            for link in soup.find_all('a'):
                ref=link.get('href')
                if valid_link(ref):
                    get_words(baseurl+ref[1:], handle, depth-1)

h=None        
# h=open(outfile,'wb')
get_words(baseurl, h, 1)
# h.close()
