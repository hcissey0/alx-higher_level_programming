#!/usr/bin/python3
"""This is a recompiled magic class"""


class MagicClass:
    """A magic class
    """

    def __init__(self, radius=0):
        """This is the instantiator"""
        self.radius = radius

    @property
    def radius(self):
        """The getter and setter for raduis"""
        return self.__radius

    @radius.setter
    def radius(self, value):
        if type(value) if not int and type(value) is not float:
            raise TypeError("radius must be a number")
        self.__radius = value

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
