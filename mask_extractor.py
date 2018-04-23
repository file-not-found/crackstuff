#!/usr/bin/env python
import string
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("file", help="password file")
args=parser.parse_args()

infile=open(args.file,'r')

for l in infile:
    mask=''
    for c in l:
        if c in string.ascii_lowercase:
            mask+='?l'
        if c in string.ascii_uppercase:
            mask+='?u'
        if c in string.punctuation:
            mask+='?s'
        if c in string.digits:
            mask+='?d'
    print(mask)
