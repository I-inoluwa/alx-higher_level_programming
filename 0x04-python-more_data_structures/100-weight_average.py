#!/usr/bin/python3

def weight_average(my_list=[]):
    if (my_list):
        score = [x[0] * x[1] for x in my_list]
        result = 0
        weight = 0
        for i, each in enumerate(score):
            result += each
            weight += my_list[i][1]

        return (result / weight)
    return (0)
