#!/usr/bin/env python

import sys
import os

PHONEBOOK_ENTRIES = []

def main():
    if len(sys.argv) < 2:
        exit(1)

    elif sys.argv[1] == "new":
        PHONEBOOK_ENTRIES.append([sys.argv[2], sys.argv[3]])

    elif sys.argv[1] == "list":
        if not os.path.isfile(PHONEBOOK_ENTRIES) or os.path.getsize(
                PHONEBOOK_ENTRIES) == 0:
            print("phonebook is empty")
        else:
            for i in PHONEBOOK_ENTRIES:
                print(str(i[0] + " " + i[1]))

    elif sys.argv[1] == "remove":
        name = sys.argv[2:]
        for i in range(len(PHONEBOOK_ENTRIES)):
            if name in PHONEBOOK_ENTRIES[i]:
                PHONEBOOK_ENTRIES.remove(i)

    elif sys.argv[1] == "clear":
        PHONEBOOK_ENTRIES.clear()



if __name__ == "__main__":
    main()
