#!/usr/bin/env python
import re
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("file", help="rule file")
args=parser.parse_args()

infile=open(args.file,'r')

regex_append='(^.*)(\$. )([^\$,\{,\},r,d]*)(\]) ?(.*$)'
regex_prepend='(^.*)(\^. )([^\^,\{,\},r,d]*)(\[) ?(.*$)'
regex_rotate1='(^.*)(\{ )([ ]*)(\}) ?(.*$)'
regex_rotate2='(^.*)(\} )( *)(\{) ?(.*$)'
regex_list=[regex_append, regex_prepend, regex_rotate1, regex_rotate2]

for line in infile:
    for regex in regex_list:
        match = re.search(regex,line)
        while match:
            line= match.group(1)+match.group(3)+match.group(5)
            match = re.search(regex,line)
    print line.rstrip()
