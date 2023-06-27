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

    def my_print(self):
        """Prints out the square with #
        """
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
