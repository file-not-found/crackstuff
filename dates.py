#!/usr/bin/env python
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-s", "--start", type=int, default=1950, 
    help="year to start from")
parser.add_argument("-e", "--end", type=int, default=2017,
    help="year to end with")
parser.add_argument("-f", "--format", type=int, choices=[1,2,3], default=3,
    help="1=DDMMYYYY, 2=MMDDYYYY, 3=both")
parser.add_argument("-d", "--delimiter", type=str, default='',
    help="delimiter between day, month and year")
args=parser.parse_args()

start=args.start
end=args.end+1
f=args.format
d=args.delimiter

for year in range(start,end):
    for month in range(1,13):
        for day in range(1,32):
            if f == 1 or f == 3:
                print("%02d%s%02d%s%d" % (day, d, month, d, year))
            if f > 1:
                print("%02d%s%02d%s%d" % (month, d, day, d, year))
