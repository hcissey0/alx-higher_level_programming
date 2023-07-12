#!/usr/bin/python3
"""This module contains a function that returns a json
representation of an object"""


import json


def to_json_string(my_obj):
    """This function returns a json repr of an object"""
    if my_obj is None:
        return
    return json.dumps(my_obj)
