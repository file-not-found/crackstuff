#!/bin/bash

case $# in
    1)
        DEBUG_MODE=1
        ;;
    2)
        case $2 in
            1)
                DEBUG_MODE=1
                ;;
            2)
                DEBUG_MODE=2
                ;;
            3)
                DEBUG_MODE=3
                ;;
            4)
                DEBUG_MODE=4
                ;;
            *)
                echo "ERROR: debug mode must be value of 1, 2, 3 or 4"
                exit 1
                ;;
        esac
        ;;
    *)
        echo "USAGE: $0 <RESULT_FILE> [<DEBUG_MODE>]"
        ;;
esac

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
DEBUG_FILE="${RULE_FILE%.rule}.debug${DEBUG_MODE}"

# clean up
rm $POT_FILE
rm $DEBUG_FILE

hashcat -m 1000 "$HASH_FILE" "$WORDLIST" -r "$RULE_FILE" --potfile-path "$POT_FILE" --debug-mode "$DEBUG_MODE" --debug-file "$DEBUG_FILE" -o /dev/null --encoding-to "$ENCODING"
