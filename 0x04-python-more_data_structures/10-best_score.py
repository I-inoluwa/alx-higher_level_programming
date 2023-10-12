#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        max_var = max(a_dictionary.keys(), key=lambda k: a_dictionary[k])
        return (max_var)
    return (None)
