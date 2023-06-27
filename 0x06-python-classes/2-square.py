#!/usr/bin/python3
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
