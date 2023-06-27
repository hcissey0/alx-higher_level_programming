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

    @property
    def position(self):
        """Getter for the position
        Returns:
            the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position
        """
        if not isinstance(value, tuple) or\
                len(value) != 2 or\
                not all(isinstance(i, int) for i in value) or\
                not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple\
                            of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints out the square with #
        """
        x, y = self.__position
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
