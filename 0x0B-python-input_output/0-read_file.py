#!/usr/bin/python3
"""This is the documentation for the module. Necessary"""


def read_file(filename=""):
    """A function that reads a text file, and prints it to stdout"""

    with (open(filename, encoding="utf-8") as f):
        lines = f.readlines()
    for each in lines:
        print(each, end="")
