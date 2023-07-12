#!/usr/bin/python3
"""This module contains a function that returns a string
from a json object"""


def from_json_string(my_str):
    """returns an object form json string"""
    import json
    if my_str is None:
        return
    return json.loads(my_str)
