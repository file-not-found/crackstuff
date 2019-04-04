#!/usr/bin/env python
import string
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("file", help="masks file")
parser.add_argument("-v","--verbose", default=False, action="store_true", help="verbose output")
parser.add_argument("-c","--count", default=False, action="store_true", help="file contains result count")
args=parser.parse_args()

infile=open(args.file,'r')

def calc(mask):
    i=1
    for c in mask[1::2]:
        if c not in 'ludhHsab':
            return 0
        if c =='l':
            i=i*26
        elif c =='u':
            i=i*26
        elif c =='d':
            i=i*10
        elif c =='h':
            i=i*16
        elif c =='H':
            i=i*16
        elif c =='s':
            i=i*33
        elif c =='a':
            i=i*95
        elif c =='b':
            i=i*256
        else:
            return 0
    return i 

for l in infile:
    if args.count:
        count=int(l[:8])
        mask=l[8:].rstrip()
    else:
        mask=l.rstrip()
    complexity=calc(mask)
    if complexity == 0:
        print("unknown format '%s'" % l.rstrip())
    else:
        if args.count:
            if args.verbose:
                print("%f %d/%d %s" % (count/complexity,count,complexity,mask))
            else:
                print("%f %s" % (count/complexity,mask))
        else:
            print("%d %s" % (complexity,mask))
