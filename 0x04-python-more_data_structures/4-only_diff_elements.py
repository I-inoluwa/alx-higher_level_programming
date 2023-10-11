#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    if (set_1 and set_2):
        new = set_1.difference(set_2).union(set_2.difference(set_1))
        return (new)

    elif set_1:
        return set_1

    elif set_2:
        return set_2

    return (set())
