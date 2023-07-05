#!/usr/bin/python3
"""
This is a module that contains only one function 'matrix_divided'
which divides a matrix by an integer
"""


def matrix_divided(matrix, div):
    """Divides a matrix by a number

    Args:
        matrix (list): list of lists
        div (in): the divider

    Returns:
        a new matrix with it's elements divided by div

    Raises:
        TypeError: when matrix is not a list or div is not an int
        ZeroDivisionError: when div is zero
    """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    size = -1
    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        if size == -1:
            size = len(i)
        elif len(i) != size:
            raise TypeError("Each row of the matrix must have \
the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        size = len(i)

    new_mat = []
    for row in matrix:
        n = []
        for i in row:
            n.append(round(i/div, 2))
        new_mat.append(n)

    return new_mat
