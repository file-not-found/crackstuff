#!/usr/bin/env python
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--minlength", type=int, default=1, 
    help="minimum length")
parser.add_argument("--maxlength", type=int, default=20,
    help="maximum length")
args=parser.parse_args()

min_len = args.minlength
max_len = args.maxlength

patterns = ['1qaz2wsx3edc4rfv5tgb6yhn7ujm', '1qazxsw23edcvfr45tgbnhy67ujm', 'q1w2e3r4t5z6u7i8o9p0', '1q2w3e4r5t6y7u8i9o0p', '1qa2ws3ed4rf5tg6yh7uj8ik9ol', 'qazwsxedcrfvtgbyhnujmik', '123qweasdzxc', 'qazxswedcvfrtgbnhyujm', 'mnbvcxz', 'lkjhgfdsa', 'poiuytrewq', '741852963', '159753', '147258369', '147852369', '741258963', '789654123', '01236547890', '09876543210', 'a1b2c3d4e5f6g7h8i9j0', '1a2b3c4d5e6f7g8h9i0j', 'qwertzuiopü+', '1234567890-=', 'abcdefghijklmnopqrstuvwxyz', '!"§$%&/()=?`', '!@#$%^&*()_+', 'qwertyuiop[]', 'asdfghjkl;\'\\', 'asdfghjklöä#', 'zxcvbnm,./', 'yxcvbnm,.-', 'azertyuiop^$', 'qsdfghjklmù*', 'wxcvbn,;:!' ]

words = set()
for p in patterns:
    for o in range(0, len(p)):
        for a in range(o+3, o+max_len+1):
            tmp = p[o:a]
            while len(tmp) <= max_len:
                if len(tmp) > min_len:
                    words.add(tmp[:max_len])
                    if 'z' in tmp or 'y' in tmp:
                        tmp2 = tmp.replace('z', 'ö')
                        tmp2 = tmp2.replace('y', 'z')
                        tmp2 = tmp2.replace('ö', 'y')
                        words.add(tmp2[:max_len])
                tmp += p[o:a]
            while len(tmp) <= max_len:
                if len(tmp) > min_len:
                    words.add(tmp[:max_len])
                    if 'z' in tmp or 'y' in tmp:
                        tmp2 = tmp.replace('z', 'ö')
                        tmp2 = tmp2.replace('y', 'z')
                        tmp2 = tmp2.replace('ö', 'y')
                        words.add(tmp2[:max_len])
                tmp += p[o:a]
cs = 'abcdefghijklmnopqrstuvwxyz0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
for a in cs:
    for length in range(min_len, max_len+1):
        words.add(a * length)
    for b in cs:
        for length in range(min_len//2, (max_len //2) +1):
            if length -1 >= min_len:
                words.add(((a + b) * length)[:-1])
            words.add((a + b) * length)
for w in words:
    print(w)
