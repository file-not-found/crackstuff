#!/usr/bin/env python3
from binascii import unhexlify
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("file")

args = parser.parse_args()

with open(args.file, "r") as infile:
    l = infile.readline().rstrip()
    while l:
        if l.startswith('$HEX['):
            h = l[l.index('[') +1 : l.index(']')]
            try:
                #print(unhexlify(h).decode("cp1252"))
                print(unhexlify(h).decode("utf-8"))
            except UnicodeDecodeError:
                pass
        else:
            print(l)
            pass
        l = infile.readline().rstrip()
