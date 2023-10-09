#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if (my_list):
        new = []
        for each in my_list:
            if (each % 2 == 0):
                new.append(True)
            else:
                new.append(False)
        return (new)
    return (my_list)
