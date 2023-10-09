#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in range(len(matrix)):
            for j, each in enumerate(matrix[i]):
                str_end = " "
                if (j == len(matrix[i]) - 1):
                    str_end = ""
                print("{:d}".format(each), end=str_end)
            print("")
