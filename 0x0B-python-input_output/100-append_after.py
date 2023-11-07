#!/usr/bin/python3
"""This is the documentation for the module. Necessary"""


def append_after(filename="", search_string="", new_string=""):
    """Appends to a file (or inserts in the line) after a string is found """

    with open(filename, mode='r', encoding='utf-8') as f:
        content = f.readlines()
        flag = 0
        for i, line in enumerate(content):
            if search_string in line:
                flag = 1
                content.insert(i + 1, new_string)
        if flag == 0:
            content.append(new_string)
    with open(filename, mode='w', encoding='utf-8') as f:
        f.writelines(content)
