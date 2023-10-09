#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if (my_list):
        new_list = []
        i = 0
        for each in my_list:
            new_list.append(my_list[i])
            if (i == idx):
                new_list[i] = element
            i += 1

        return (new_list)
    return (my_list)
