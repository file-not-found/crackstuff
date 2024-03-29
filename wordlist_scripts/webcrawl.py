#!/usr/bin/env python3
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("url", help="url to start from")
parser.add_argument("-d", "--depth", type=int, default=1,
    help="crawling depth")
args=parser.parse_args()

baseurl = '/'.join(args.url.split('/')[:3])

nogo=('css','js','pdf')

def valid_link(ref):
    if not ref:
        return False
    elif not ref[0] == '/':
        return False
    elif ref.split('.')[-1] in nogo:
        return False
    else:
        return True

def get_words(url, depth):
    req= Request(url)
    req.add_header('User-Agent','Mozilla/5.0')
    try:
        resp= urlopen(req)
    except:
        return
    html= resp.read()

    soup=BeautifulSoup(html, 'html.parser')

    try:
        text=soup.body.text
    except:
        text=None

    if text != None:
        for word in text.split():
            print(word)
    
        if depth > 0:
            for link in soup.find_all('a'):
                ref=link.get('href')
                if valid_link(ref):
                    get_words(baseurl+ref, depth-1)

get_words(args.url, args.depth)
