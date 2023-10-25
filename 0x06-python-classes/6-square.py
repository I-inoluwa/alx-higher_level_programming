#!/usr/bin/python3
"""Oh! This needs a documentation too."""


class Square:
    """Creates a square with an attribute."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square with a size attribute

        Attributes:
            size: The size of the square. Initialised to 0.
            position: a positional argument. Usually a tuple.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        if type(position) == tuple:
            try:
                int(position[0])
                int(position[1])
                if position[0] < 0 or position[1] < 0:
                    raise Exception
            except Exception:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

        self._Square__size = size
        self._Square__position = position

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

    def my_print(self):
        """Prints out the square in matrix form"""

        if (self.size == 0):
            print("")
        for i in range(self.size):
            if (self.position[1] <= 0):
                print(" " * self.position[0] + "#" * self.size)
            else:
                print("#" * self.size)

    @property
    def position(self):
        """returns the value of the position given"""

        return (self._Square__position)

    @position.setter
    def position(self, value):
        """Sets the value of a position

        Attributes:
            value: the value to set positional argument with.
        """

        if type(value) == tuple:
            try:
                int(value[0])
                int(value[1])
                if value[0] < 0 or value[1] < 0:
                    raise Exception
            except Exception:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

        self._Square__position = value
        return (value)
