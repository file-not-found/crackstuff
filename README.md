# crackstuff

Some files and scripts to help cracking passwords during a penetration test.
For some notes on cracking and wordlist creation see 
[http://exitno.de/cracking/](http://exitno.de/cracking/).

## scripts

* `cleanup_rules.py` uses regex to cleanup hashcat rules
* `dates.py` prints 8 digit dates as MMDDYYYY and DDMMYYYY
* `easy_patterns.py` prints easy character patterns and repetitions
* `list_combine.py` combines every word from two text files
* `mask_extractor.py` generate hashcat mask files from found passwords
* `mask_eval.py` calculate quality of masks from brute force results
* `webcrawl.py` prints every word found in the body of a website

## masks

Mask files for `hashcat`. 

## rules

The rules in `clean.rule` are optimized for lowercase words but work for 
password lists like `rockyou.txt` as well.  They are roughly sorted by quality. 
To create smaller rulesets use `head -n `.

## wordlists

Some wordlists coverted to lowercase. Files with `+` in their names contain 
additional words.
