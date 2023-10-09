#!/usr/bin/python3

def element_at(my_list, idx):
    i = 0
    for each in my_list:
        if (i == idx):
            return (each)
        i += 1
    
    return(None)

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
