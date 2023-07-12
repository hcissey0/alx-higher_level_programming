#!/usr/bin/python3
"""This module inserts strings"""


def append_after(filename="", search_string="", new_string=""):
    """appends a string after a specific string in a file"""
    with open(filename, "r+") as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
        f.truncate()
