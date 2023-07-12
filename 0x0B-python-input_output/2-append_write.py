#!/usr/bin/python3
"""This module contains one function that appends to a file"""


def append_write(filename="", text=""):
    """this functions appends texts to the end of a file"""
    if filename is None or type(filename) is not str:
        return
    a = 0
    with open(filename, "a") as f:
        a = f.write(text)
    return a
