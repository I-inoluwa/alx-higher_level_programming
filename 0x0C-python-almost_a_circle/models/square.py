#!/usr/bin/python3
"""Module Documentation: Creates a square. Inherits from rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from the previously created Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialisation of the square class."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """retrieves the size of the rectangle"""
        return (self._Rectangle__width)

    @size.setter
    def size(self, value):
        """Sets the width of the rectangle with a value."""
        self._Rectangle__validate_non_negative_integer("width", value)
        self._Rectangle__width = value
        return (value)

    def __str__(self):
        """Returns a string literal of the class"""
        return (f"[Square] ({self.id:d}) {self.x:d}/{self.y:d} - {self.size}")

    def update(self, *args, **kwargs):
        """Updates all values of all the arguments"""
        arr = "id size x y".split()
        if args:
            for i, each in enumerate(args):
                setattr(self, arr[i], each)
        else:
            for key, value in kwargs.items():
                setattr(self, str(key), value)
