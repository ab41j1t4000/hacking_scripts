#!/bin/bash

read -p "Please enter the Max length of the password that should be generated: " MAX_LEN
read -p "Please enter the number of passwords to generate: " PASS_NO

for p in $(seq 1 $PASS_NO);
do
	echo ""
	openssl rand -base64 48 | cut -c1-$MAX_LEN
done

