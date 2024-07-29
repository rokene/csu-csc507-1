#!/usr/bin/env bash

echo $RANDOM > file1.txt

for i in {1..999}; do
  echo $RANDOM >> file1.txt
done

cat file1.txt
rm file1.txt
