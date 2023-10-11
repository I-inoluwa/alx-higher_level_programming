#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list:
        new_list = set(my_list)
        result = 0
        for each in new_list:
            result += each
        return (result)
    return (0)
