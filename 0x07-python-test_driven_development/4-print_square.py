#!/usr/bin/python3
"""this module contains a function print_square that prints a square with #
"""


def print_square(size):
    """This function prints a square with #
    Args:
        size (int): the square size
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
