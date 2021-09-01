#!/bin/bash

INPUT_FILE=$1
OUTPUT_FILE="${INPUT_FILE%.*}.result"
if [ ! -e "$INPUT_FILE" ]
then
    echo "file not found $INPUT_FILE"
    exit 1
fi

echo "counting rules from $INPUT_FILE"
echo "creating new file $OUTPUT_FILE"

sort "$INPUT_FILE" | uniq -c | sort -rn > "$OUTPUT_FILE"
