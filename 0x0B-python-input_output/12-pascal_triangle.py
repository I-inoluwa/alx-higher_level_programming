#!/usr/bin/python3
"""This is the documentation for the module. Necessary"""


def pascal_triangle(n):
    """Returns the pascal triangle for a given integer 'n'."""

    if n <= 0:
        return ([])

    prev = []
    retval = []
    for i in range(n):
        new = [1]
        for j in range(len(prev)):
            if j == len(prev) - 1:
                new.append(1)
            else:
                new.append(prev[j] + prev[j + 1])
        retval.append(new)
        prev = new[:]

    return retval
