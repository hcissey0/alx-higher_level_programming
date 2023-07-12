#!/usr/bin/python3
"""This module contains a function that prints
a file content"""


def read_file(filename=""):
    """This function prints a file content"""
    if filename is None or type(filename) is not str:
        return
    with open(filename, "r") as f:
        print(f.read(), end="")
