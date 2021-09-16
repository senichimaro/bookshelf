#!/bin/bash

DEFAULT_ENDPOINT="http://localhost:5000"
API_ENDPOINT="$1"
API_ENDPOINT=${API_ENDPOINT:=$DEFAULT_ENDPOINT}

(
    cd $(dirname $0)

    # colors
    COLOR_GREEN="$(tput setaf 2)"

    TEST_NUMBER=1
    cat test_cases.txt | egrep -v '^#' | while read line
    do
        INPUT=$(echo "$line" | cut -d"|" -f1)

        if [ "$INPUT" != "" ]
        then
            OUTPUT=$(curl --silent \
                -H "Content-Type: application/json" \
                -X POST \
                -d "$INPUT" \
                "$API_ENDPOINT/books"
            )

            echo "${COLOR_GREEN}$TEST_NUMBER Target: "$INPUT""

            TEST_NUMBER=$((TEST_NUMBER+1))
        fi
    done
)