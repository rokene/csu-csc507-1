#!/usr/bin/env bash

echo "### processor info ###############################"
echo ""

lscpu

echo ""

echo "### main memory info ###############################"
echo ""

free -h

echo ""

echo "### i/o info ###############################"
echo ""

lspci

echo ""

echo "### storage info ###############################"
echo ""

lsblk

echo ""

