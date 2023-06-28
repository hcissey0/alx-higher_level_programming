#!/usr/bin/python3
import math
"""This is a recompiled magic class"""


class MagicClass:
    """A magic class
    """

    def __init__(self, radius=0):
        """This is the instantiator"""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Finds the area of the circle

        Returns:
            the area
        """
        return (math.pi * self.__radius ** 2)

    def circumference(self):
        """
        Finds the circumference

        Returns:
            the circumference
        """
        return (2 * math.pi * self.__radius)
