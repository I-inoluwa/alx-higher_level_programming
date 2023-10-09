#!/usr/bin/python3

def max_integer(my_list=[]):
    if (my_list):
        max = my_list[0]
        for each in my_list:
            if each > max:
                max = each
        return (max)
    return (None)
