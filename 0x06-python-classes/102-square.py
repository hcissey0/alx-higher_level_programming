#!/usr/bin/python3
"""Defines a square"""


class Square:
    """This is a square Class
    """
    def __init__(self, size=0):
        """This is the constructor

        Args:
            size: the size of the square

        Raises:
            TypeError: when size is not an int
            ValueError: when size is < 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """This is the area of the square

        Returns:
            the area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """The getter  function for size

        Returns:
            The size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """The setter function for size

        Args:
            value (int): the value to set
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """
        Checks for equals
        """
        return self.area() == other.area()

    def __lt__(self, other):
        """
        Checks for less than
        """
        return self.area() < other.area()

    def __gt__(self, other):
        """
        Checks for greater than
        """
        return self.area() > other.area()

    def __le__(self, other):
        """
        Checks for less than or equal to
        """
        return self.area() <= other.area()

    def __ge__(self, other):
        """
        Checks for greater than or equal to
        """
        return self.area() >= other.area()

    def __ne__(self, other):
        """
        Checks for not equal to
        """
        return self.area() != other.area()
