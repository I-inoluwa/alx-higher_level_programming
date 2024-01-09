#!/usr/bin/python3
"""This is the documentation for the module. Necessary"""


def append_write(filename="", text=""):
    """Function to append a string of text to a file"""
    with open(filename, mode='a', encoding='utf-8') as f:
        num = f.write(text)

    return (num)
