#!/usr/bin/python3
"""This is the documentation for the module. Very necessary
Add more lines
"""


def read_file(filename=""):
    """A function that reads a text file, and prints it to stdout"""
    with (open(filename, encoding="utf-8") as f):
        for each in f:
            print(each, end="")
