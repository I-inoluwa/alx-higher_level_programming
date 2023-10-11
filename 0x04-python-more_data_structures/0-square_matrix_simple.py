#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix:
        new_matrix = []
        for each in matrix:
            row = [x**2 for x in each]
            new_matrix.append(row)

        return (new_matrix)
    return (matrix)
