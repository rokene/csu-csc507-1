#!/usr/bin/env bash

start_time=$(date +%s)

NUMBERS_FILE=file1.txt
NUMBERS_OUTPUT=newfile1.txt

while read -r number; do
    double=$((number * 2))
    echo $double >> $NUMBERS_OUTPUT
done < $NUMBERS_FILE

end_time=$(date +%s)
elapsed_time=$((end_time - start_time))
num_count=$(wc -l < "$NUMBERS_FILE")

echo "Time taken to double ${num_count} numbers: $elapsed_time seconds"
