#!/usr/bin/python3
"""This is the documentation for the module. Necessary"""


def append_after(filename="", search_string="", new_string=""):
    """Appends to a file (or inserts in the line) after a string is found """

    with open(filename, mode='r', encoding="utf-8") as f:
        content = []
        for line in f:
            content.append(line)
            if search_string in line:
                content.append(new_string)

    with open(filename, mode='w', encoding='utf-8') as g:
        g.writelines(content)
