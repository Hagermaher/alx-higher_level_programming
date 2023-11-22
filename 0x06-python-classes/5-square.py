#!/usr/bin/python3

"""Define class Square"""


class Square:
    """Represent square"""

    def __init__(self, size):
        """Initialize a new square

        Args:
            size (int): size of the new square
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        for w in range(0, self.__size):
            [print("#", end="") for g in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
