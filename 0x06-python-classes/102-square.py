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

    @property
    def size(self):
        """retrieves the size of the square"""

        return (self._Square__size)

    @size.setter
    def size(self, value):
        """Sets the size of the square with a value.

        Attributes:
            value: value to replace square size.
        """

        if type(value) != int:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")

        self._Square__size = value
        return (value)

    def __eq__(self, value):
        """Checks for equality"""

        return (self.size == value.size)

    def __ne__(self, value):
        """Checks for non-equality"""

        return (self.size != value.size)

    def __lt__(self, value):
        """Compares if self is less than other"""

        return (self.size < value.size)

    def __gt__(self, value):
        """Compares if self is greater than other"""

        return (self.size > value.size)

    def __le__(self, value):
        """Compares if self is less than or equal to other"""

        return (self.size <= value.size)

    def __ge__(self, value):
        """Compares if self is greater than or equal to other"""

        return (self.size >= value.size)
