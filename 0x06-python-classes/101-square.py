#!/usr/bin/python3
"""Defines a square"""


class Square:
    """This is a square Class
    """
    def __init__(self, size=0, position=(0, 0)):
        """This is the constructor

        Args:
            size: the size of the square

        Raises:
            TypeError: when size is not an int
            ValueError: when size is < 0
        """
        self.size = size
        self.position = position

    def area(self):
        """The area of the square

        Returns:
            the area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """The getter and setter functions for size
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter and setter for the position
        Returns:
            the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or\
                len(value) != 2 or\
                not all(isinstance(i, int) for i in value) or\
                not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints out the square with #
        """
        if self.size == 0:
            print()
            return
        print("\n" * self.position[1], end="")
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """
        Prints the square instance
        """
        res = ''
        if self.size == 0:
            return '\n'
        res += '\n' * self.position[1]
        for _ in range(self.size):
            res += " " * self.position[0] + "#" * self.size + '\n'
        return res
