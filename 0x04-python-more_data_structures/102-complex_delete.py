#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if a_dictionary:
        ls = list(a_dictionary.keys())
        for i in range(len(ls)):
            if (a_dictionary[ls[i]] == value):
                a_dictionary.pop(ls[i])
    return (a_dictionary)
