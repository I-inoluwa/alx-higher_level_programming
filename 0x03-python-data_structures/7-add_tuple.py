#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    while (len(tuple_a) < 2) or (len(tuple_b) < 2):
        if (len(tuple_a) < 2):
            tuple_a = list(tuple_a)
            tuple_a.append(0)
        if (len(tuple_b) < 2):
            tuple_b = list(tuple_b)
            tuple_b.append(0)

    a = tuple_a[0] + tuple_b[0]
    b = tuple_a[1] + tuple_b[1]

    return (a, b)
