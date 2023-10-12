#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if a_dictionary:
        new = {x: y for x, y in a_dictionary.items() if y != value}
        return (new)
    return (a_dictionary)
