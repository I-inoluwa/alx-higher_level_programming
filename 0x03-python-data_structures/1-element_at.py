#!/usr/bin/python3
def element_at(my_list, idx):
    i = 0
    for each in my_list:
        if (i == idx):
            return (each)
        i += 1

    return(None)
