#!/usr/bin/python3
"""This is the documentation for the module. Necessary"""


def write_file(filename="", text=""):
    """Function to write a string of text to a file"""
    with open(filename, mode='w', encoding='utf-8') as f:
        num = f.write(text)

    return (num)
