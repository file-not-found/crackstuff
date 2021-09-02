#!/usr/bin/env python3
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("file1", help="first file")
parser.add_argument("file2", nargs='?', default=None, help="second file")
parser.add_argument("-d", "--delimiter", type=str, default=' ',
    help="delimiter between words")
parser.add_argument("--double", action="store_true",
    help="combine equal words")
args=parser.parse_args()

d = args.delimiter

f1=open(args.file1,'r')
h1=f1.readlines()

if args.file2 != None:
    f2=open(args.file2,'r')
    h2=f2.readlines()
else:
    h2=h1

for l1 in h1:
    for l2 in h2:
        w1=l1.rstrip()
        w2=l2.rstrip()
        if len(w1) == 0:
            print(l2.rstrip())
        elif len(w2) == 0:
            print(l1.rstrip())
        elif not w1 == w2 or args.double:
            print("%s%s%s" % (w2, d ,w1))
