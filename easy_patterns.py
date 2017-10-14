#!/usr/bin/env python
from math import floor, ceil
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--minlength", type=int, default=1, 
    help="minimum length")
parser.add_argument("--maxlength", type=int, default=20,
    help="maximum length")
parser.add_argument("-k", "--keyboard", type=str, choices=['d','u','b'],
    default='b', help="keyboard layout: (d)e, (u)s, (b)oth")
args=parser.parse_args()

min_len = args.minlength
max_len = args.maxlength
k = args.keyboard

charsets = {
    'numbers_u'     : '1234567890-=',
    'numbers_d'     : '1234567890ß´',
    'letters_b'     : 'abcdefghijklmnopqrstuvwxyz',
    'keyboard0_u'   : '!@#$%^&*()_+',
    'keyboard0_d'   : '!"§$%&/()=?`',
    'keyboard1_u'   : 'qwertyuiop[]',
    'keyboard1_d'   : 'qwertzuiopü+',
    'keyboard2_u'   : 'asdfghjkl;\'\\',
    'keyboard2_d'   : 'asdfghjklöä#',
    'keyboard3_u'   : 'zxcvbnm,./',
    'keyboard3_d'   : 'yxcvbnm,.-',
}
for n, cs in charsets.items():
    if n[-1:] == k or n[-1] == 'b' or k == 'b':
        for end in range(2,len(cs)+1):
            for repeat in range(ceil(min_len/end),floor(max_len/end)+1):
                print(cs[:end]*repeat)

cs = 'abcdefghijklmnopqrstuvwxyz0123456789!"§#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
if k in ['b','d']:
    cs += 'öäüß'
for c in cs:
    for length in range(min_len, max_len+1):
        print(c*length)
