#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        return [[x**2 for x in y] for y in matrix]
