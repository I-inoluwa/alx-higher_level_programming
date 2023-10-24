#!/usr/bin/python3
"""Oh! This needs a documentation too."""


class Square:
    """Creates a square with an attribute."""

    def __init__(self, size=0):
        """Initializes a square with a size attribute

        Attributes:
            size: The size of the square. Initialised to 0.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

        self._Square__size = size

    def area(self):
        """returns the area of the square"""

        return (self._Square__size ** 2)
