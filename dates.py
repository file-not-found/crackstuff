#!/usr/bin/env python
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-s", "--start", type=int, default=1950, 
    help="year to start from")
parser.add_argument("-e", "--end", type=int, default=2017,
    help="year to end with")
parser.add_argument("-f", "--format", type=int, choices=[1,2,3,4,5], default=3,
    help="1=DDMMYYYY, 2=MMDDYYYY, 3=DDmonthYYYY, 4=DDmonYYYY, 5=all")
parser.add_argument("-d", "--delimiter", type=str, default='',
    help="delimiter between day, month and year")
parser.add_argument("-r","--rules", default=False, action="store_true", help="generate as hashcat rules")
args=parser.parse_args()

months=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
        'September', 'October', 'November', 'December']

start=args.start
end=args.end+1
f=args.format
d=args.delimiter

for year in range(start,end):
    for month in range(1,13):
        for day in range(1,32):
            if f == 1 or f == 5:
                date=("%02d%s%02d%s%d" % (day, d, month, d, year))
                if args.rules:
                    print('$' + ' $'.join(date))
                else:
                    print(date)
            if f == 2 or f == 5:
                date=("%02d%s%02d%s%d" % (month, d, day, d, year))
                if args.rules:
                    print('$' + ' $'.join(date))
                else:
                    print(date)
            if f == 3 or f == 5:
                date=("%02d%s%s%s%d" % (day, d, months[month-1], d, year))
                if args.rules:
                    print('$' + ' $'.join(date))
                else:
                    print(date)
            if f == 4 or f == 5:
                date=("%02d%s%s%s%d" % (day, d, months[month-1][:3], d, year))
                if args.rules:
                    print('$' + ' $'.join(date))
                else:
                    print(date)
