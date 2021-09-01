#!/bin/bash

INPUT_FILE="$1"
INPUT_EXT="rule"

if [ "${INPUT_FILE##*.}" != "$INPUT_EXT" ]
then
    echo "unexpected extension ${INPUT_FILE##*.}"
    exit 1
fi

if [ ! -e "$INPUT_FILE" ]
then
    echo "file not found $INPUT_FILE"
    exit 1
fi

RULE_FILE=$INPUT_FILE
HASH_FILE=hashes.ntlm
WORDLIST=words.txt
ENCODING="cp1252"
POT_FILE="${RULE_FILE%.rule}.pot"

# clean up
rm ${RULE_FILE%.rule}_*.rule
rm ${RULE_FILE%.rule}_*.debug1

# split rules
for i in {1..40}; do cat "$RULE_FILE" | grep -P "^(((l|u|c|C|t|T.|r|d|p.|f|\{|\}|\\\$.|\^.|\[|\]|D.|x..|O..|i..|o..|\'.|s..|@.|z.|Z.|q|X...|4|6|M|k|K|\*..|L.|R.|\+.|\-.|\..|\,.|y.|Y.|E|e.) ?){$i}\$)" > "${RULE_FILE%.rule}_$i.rule"; done
find . -iname "${RULE_FILE%.rule}_*.rule" -size 0 -delete

# crack short to long
if [ $# -eq 2 ] && [ $2 = "reverse" ]
then
    for i in {40..1}; do if [ -e "${RULE_FILE%.rule}_$i.rule" ]; then hashcat -m 1000 "$HASH_FILE" "$WORDLIST" -r "${RULE_FILE%.rule}_$i.rule" --potfile-path "$POT_FILE" --debug-mode 1 --debug-file "${RULE_FILE%.rule}_$i.debug1" -o /dev/null --encoding-to "$ENCODING"; fi; done
else
    for i in {1..40}; do if [ -e "${RULE_FILE%.rule}_$i.rule" ]; then hashcat -m 1000 "$HASH_FILE" "$WORDLIST" -r "${RULE_FILE%.rule}_$i.rule" --potfile-path "$POT_FILE" --debug-mode 1 --debug-file "${RULE_FILE%.rule}_$i.debug1" -o /dev/null --encoding-to "$ENCODING"; fi; done
fi

# concat results
cat ${RULE_FILE%.rule}_*.debug1 > ${RULE_FILE%.rule}.debug1

# clean up again
rm ${RULE_FILE%.rule}_*.rule
rm ${RULE_FILE%.rule}_*.debug1
