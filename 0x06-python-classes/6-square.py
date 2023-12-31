#!/usr/bin/python3

"""Define class Square."""


class Square:
    """Represent square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize new square.

        Args:
            size (int): size
            position (int, int): position
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get/set the current position of squar."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return current area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for w in range(0, self.__position[1])]
        for w in range(0, self.__size):
            [print(" ", end="") for g in range(0, self.__position[0])]
            [print("#", end="") for q in range(0, self.__size)]
            print("")
