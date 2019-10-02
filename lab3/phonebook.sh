#!/bin/bash

PHONEBOOK_ENTRIES=""


if [ "$# -lt 1 ]; then
	exit 1

elif [ "$1" = "new" ]; then
	PHONEBOOK_ENTRIES += "$2" + " " + "$3"

elif [ "$1" = "list" ]; then
	if [ ! -e $PHONEBOOK_ENTRIES ] || [ ! -s $PHONEBOOK_ENTRIES ]; then
		echo "phonebook is empty"
	else
		echo PHONEBOOK_ENTRIES
	fi

elif [ "$1" = "remove" ]; then
	tr -d PHONEBOOK_ENTRIES $2 $3

elif [ "$1" = "clear"]; then
	PHONEBOOK_ENTRIES = ""

else
	echo PHONEBOOK_ENTRIES
fi
