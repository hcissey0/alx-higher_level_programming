#!/usr/bin/python3
"""
This module defines a function that adds two integers
"""


def add_integer(a, b=98):
    """This is function adds two integers

    Args:
        a: the first integer
        b: the second integer, 98 default

    Returns:
        the sum of a and b

    Raises:
        TypeError: when a or b is not an integer or float
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
