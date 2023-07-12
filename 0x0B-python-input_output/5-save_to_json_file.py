#!/usr/bin/python3
"""This module contains a function that saves an object
to a json file"""


def save_to_json_file(my_obj, filename):
    """This func saves an object to a json file"""
    import json
    if filename is None or type(filename) is not str:
        return
    with open(filename, "w") as f:
        f.write(json.JSONEncoder().encode(my_obj))
