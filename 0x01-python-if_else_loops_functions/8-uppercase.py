#!/usr/bin/python3

def uppercase(str):
    i = 0
    c = 0
    for c in str:
        if (ord(c) >= 97 and ord(c) <= 122):
            c = ord(c) - 32
        else:
            c = ord(c)

        print("{:c}".format(c), end="")

        if (i == len(str) - 1):
            break

        i += 1

    print("")
