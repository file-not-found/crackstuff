#!/usr/bin/env python3

format_both = ["{}", "c {}", "u {}", "{} $!", "{} $?", "c {} $!", "c {} $?",]
format_append = ["^1 {}", "^1 ^1 {}",  "$_ {}", "$- {}", "$@ {}", "$. {}", "c ^1 {}", "c ^1 ^1 {}",  "c $_ {}", "c $- {}", "c $@ {}", "c $. {}",]
format_prepend = ["{} $1 $2", "{} $1 $1", "^_ {}", "^. {}", "c {} $1 $2", "c {} $1 $1", "c ^_ {}", "c ^. {}"]

splityear = 50

def print_format(year):
    a = "$" + " $".join(c for c in year)
    p = "^" + " ^".join(c for c in year[::-1])
    for f in format_both:
        print(f.format(p))
        print(f.format(a))
    for f in format_append:
        print(f.format(a))
    for f in format_prepend:
        print(f.format(p))

for i in range(100):
    year = "{:02d}".format(i)
    print_format(year)
    if i < splityear:
        print_format("20" + year)
    else:
        print_format("19" + year)
