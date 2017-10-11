#!/usr/bin/env python
from math import floor, ceil
min_len = 1
max_len = 20
charsets = {
    'numbers'   : '1234567890-=',
    'numbersg'  : '1234567890ß´',
    'letters'   : 'abcdefghijklmnopqrstuvwxyz',
    'keyboard0' : '!@#$%^&*()_+',
    'keyboard0g': '!"§$%&/()=?`',
    'keyboard1' : 'qwertyuiop[]',
    'keyboard1g': 'qwertzuiopü+',
    'keyboard2' : 'asdfghjkl;\'\\',
    'keyboard2g': 'asdfghjklöä#',
    'keyboard3' : 'zxcvbnm,./',
    'keyboard3g': 'yxcvbnm,.-',
}
for cs in charsets.values():
    for end in range(2,len(cs)+1):
        for repeat in range(ceil(min_len/end),floor(max_len/end)+1):
            print(cs[:end]*repeat)

cs = 'abcdefghijklmnopqrstuvwxyz0123456789!"§#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~öaüß'
for c in cs:
    for length in range(min_len, max_len+1):
        print(c*length)
