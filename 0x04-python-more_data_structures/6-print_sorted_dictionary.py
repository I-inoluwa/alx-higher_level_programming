#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if (a_dictionary):
        for each in sorted(a_dictionary.keys()):
            print("{}: {}".format(each, a_dictionary[each]))
