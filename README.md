# crackstuff

Some files and scripts to help cracking passwords during a penetration test.
For some notes on cracking and wordlist creation see 
[http://exitno.de/cracking/](http://exitno.de/cracking/).

## benchmark\_scripts

* `count_entries.sh` creates file with sorted count of identical lines
* `extract_results.sh` truncates count value from result file
* `remove_cracked_hashes.sh` remove cracked hashes from hash file
* `crack_debug.sh` run default hashcat command
* `crack_short_first.sh` run hashcat with rules split by length

## hash\_scripts

* `dcc2_convert.sh` convert dcc2 hash file to hashcat format

## mask\_scripts

* `mask_eval.py` calculate quality of masks from brute force results
* `mask_extractor.py` generate hashcat mask files from found passwords

## rule\_scripts

* `cleanup_rules.py` uses regex to cleanup hashcat rules
* `complexity_filter.sh` filters rules for resulting password complexity
* `year_rules` create hashcat rules containing year values

## wordlist\_scripts

* `dates.py` prints 8 digit dates as MMDDYYYY and DDMMYYYY
* `patterns.py` prints some character patterns and repetitions
* `list_combine.py` combines every word from two text files
* `webcrawl.py` prints every word found in the body of a website

## masks

Mask files for `hashcat`. 

## rules

`hashcat` rules

## wordlists

Some wordlists.
