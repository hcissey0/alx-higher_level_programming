#!/usr/bin/python3
"""This is the base class of all other classes in this project"""


class Base:
    """This is the Base class to manage id"""

    __nb_objects = 0

    def __init__(self, id=None):
        """This is the classes initializor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
