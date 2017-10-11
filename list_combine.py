#!/usr/bin/env python
file1=  'small.rule'
file2=  'combo.rule'

f1=open(file1,'r')
f2=open(file2,'r')

h1=f1.readlines()
h2=f2.readlines()
#h2=h1

for l1 in h1:
    for l2 in h2:
        w1=l1.rstrip()
        w2=l2.rstrip()
        if len(w1) == 0:
            print(l2.rstrip())
        elif len(w2) == 0:
            print(l1.rstrip())
        elif not w1 == w2:
            print("%s %s" % (w2,w1))
    f2.seek(0)
