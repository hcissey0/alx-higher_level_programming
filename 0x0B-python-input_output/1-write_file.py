#!/usr/bin/python3
"""This module contains a function that writes to a file"""


def write_file(filename="", text=""):
    """This function writes to a file"""
    if filename is None or type(filename) is not str:
        return
    a = 0
    with open(filename, "w") as f:
        a = f.write(text)
    return a
