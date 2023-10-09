#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if (my_list):
        i = 0
        j = -1
        new_list = []
        length = len(my_list)
        for i in range(length):
            if (i == idx):
                j = i
            else:
                new_list.append(my_list[i])
        if (j >= 0):
            del (my_list[j])
        return (new_list)
    return (my_list)
