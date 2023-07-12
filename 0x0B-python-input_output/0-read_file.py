#!/usr/bin/python3
def read_file(filename=""):
    """This function prints a file content"""
    if filename is None or type(filename) is not str:
        return
    with open(filename, "r") as f:
        print(f.read(), end="")
