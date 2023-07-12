#!/usr/bin/python3
"""This module contains a class"""


class Student():
    """This is a student class"""

    def __init__(self, first_name, last_name, age):
        """The initializor of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dict repr of a Student"""
        if attrs is None:
            attrs = self.__dict__.keys()
        at = {k: v for k, v in self.__dict__.items() if k in attrs}
        return at

    def reload_from_json(self, json):
        """replaces all attributes with json attrubutes"""
        for k, v in json.items():
            setattr(self, k, v)
