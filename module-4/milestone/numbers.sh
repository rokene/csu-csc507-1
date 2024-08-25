#!/usr/bin/env bash

SECONDS=0
NUMBERS_FILE=file1.txt

echo "processing numbers"

echo $RANDOM > $NUMBERS_FILE

for i in {1..999999}; do
  echo $RANDOM >> $NUMBERS_FILE
done

duration=$SECONDS

NUMBERS_COUNT=$(wc -l < "$NUMBERS_FILE")

echo "Processing ${NUMBERS_COUNT} numbers took $((duration / 3600)) hours, $(((duration / 60) % 60)) minutes, $((duration % 60)) seconds."
