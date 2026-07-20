#!/usr/bin/python3
"""Defines a Square class inheriting from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initializes a Square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square.

        Returns:
            int: The area (size * size).
        """
        return self.__size ** 2

    def __str__(self):
        """Returns a string representation of the square.

        Returns:
            str: The square description.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
