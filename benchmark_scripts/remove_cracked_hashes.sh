#!/bin/bash

INPUT_FILE="$1"
INPUT_EXT="pot"

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

POT_FILE=$INPUT_FILE
OLD_HASHES=hashes.ntlm
NEW_HASHES=hashes.uncracked

echo "extracting hashes from $POT_FILE and removing them from $OLD_HASHES"
echo "creating new file $NEW_HASHES"

comm -13 <(cat "$POT_FILE" | cut -d ':' -f 1  | tr 'ABCDEF' 'abcdef' | sort -u) <( cat "$OLD_HASHES" | tr 'ABCDEF' 'abcdef' | sort -u) > "$NEW_HASHES"
