#!/bin/bash

case $# in
    1)
        GREP=""
        ;;
    2)
        case $2 in
            10)
                GREP="^      "
                ;;
            100)
                GREP="^     "
                ;;
            1000)
                GREP="^    "
                ;;
            10000)
                GREP="^   "
                ;;
            *)
                echo "ERROR: minimum matches must be value of 10, 100, 1000 or 10000"
                exit 1
                ;;
        esac
        ;;
    *)
        echo "USAGE: $0 <RESULT_FILE> [10|100|1000|10000]"
        ;;
esac
#exit 0
RESULT_FILE=$1
if [ "${RESULT_FILE##*.}" != "result" ]
then
    echo "unexpected extension ${RESULT_FILE##*.}"
    exit 1
fi
if [ -z "$GREP" ]
then
    OUTPUT_FILE="${RESULT_FILE%.*}.out"
    echo "counting rules from $RESULT_FILE"
    echo "creating new file $OUTPUT_FILE"

    cat "$RESULT_FILE" | cut -b 9- > "$OUTPUT_FILE"
else
    OUTPUT_FILE="${RESULT_FILE%.*}_$2.out"
    echo "counting rules from $RESULT_FILE"
    echo "creating new file $OUTPUT_FILE"

    cat "$RESULT_FILE" | grep -v "$GREP" | cut -b 9- > "$OUTPUT_FILE"
fi
