#!/bin/bash

echo "This is a file encrypter-decrypter"
echo "Please specify what you want to do"
choice="Encrypt Decrypt"
select option in $choice; do
if [ $REPLY = 1 ];
then
	echo "You have selected encryption"
	ls
	echo ""
	echo "Please specify the file name"
	read FILE;
	gpg -c $FILE
	echo "The file has been encrypted"
	exit;
else
	echo "You have selected decryption"
	ls
	echo ""
	echo "Please specify a file name"
	read FILE1;
	gpg -d $FILE1
	echo "The file has been decrypted"
	exit;
fi
done
