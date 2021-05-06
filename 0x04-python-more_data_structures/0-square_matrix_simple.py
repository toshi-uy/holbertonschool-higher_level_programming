#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for sublist in matrix:
        row = []
        for item in sublist:
            row.append(item**2)
        result.append(row)
    return result
