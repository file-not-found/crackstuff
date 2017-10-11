#!/usr/bin/env python
for day in range(1,32):
    for month in range(1,13):
        for year in range(1940,2011):
            print("%02d%02d%d" % (day, month, year))
            print("%02d%02d%d" % (month, day, year))
