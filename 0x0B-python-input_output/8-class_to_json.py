#!/usr/bin/python3
"""This module has only one function"""


def class_to_json(obj):
    """This function converts a class to a json object"""
    import json
    at = {k: v for k, v in obj.__dict__.items() if not k.startswith("__")}
    return (at)
