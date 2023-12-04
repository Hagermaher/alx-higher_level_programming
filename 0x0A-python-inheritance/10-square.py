#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent square."""

    def __init__(self, size):
        """Initialize square

        Args:
            size (int): The size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
