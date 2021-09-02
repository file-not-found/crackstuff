#!/usr/bin/env python3
import string
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("file", help="password file")
args=parser.parse_args()

infile=open(args.file,'r')

for l in infile:
    mask=''
    for c in l.rstrip('\n'):
        if c in string.ascii_lowercase:
            mask+='?l'
        elif c in string.ascii_uppercase:
            mask+='?u'
        elif c in string.punctuation+" ":
            mask+='?s'
        elif c in string.digits:
            mask+='?d'
    print(mask)
