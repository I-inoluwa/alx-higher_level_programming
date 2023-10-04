#!/usr/bin/python3

def uppercase(str):
    i = 0
    for c in str:
        if (ord(c) >= 97 and ord(c) <= 122):
            c = ord(c) - 32
        else:
            c = ord(c)

        if (i == len(str) - 1):
            print("{:c}".format(c), end="\n")
        else:
            print("{:c}".format(c), end="")
        i += 1
