#!/usr/bin/python3
"""Module Documentation: Creates a rectangle. Inherits from base"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class created, to inherit from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialisation of the Rectangle class"""
        super().__init__(id=id)
        self.__validate_non_negative_integer("width", width)
        self.__validate_non_negative_integer("height", height)
        self.__validate_non_negative_integer("x", x)
        self.__validate_non_negative_integer("y", y)

        self._Rectangle__width = width
        self._Rectangle__height = height
        self._Rectangle__x = x
        self._Rectangle__y = y

    @property
    def width(self):
        """retrieves the width of the rectangle"""
        return (self._Rectangle__width)

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle with a value."""
        self.__validate_non_negative_integer("width", value)
        self._Rectangle__width = value
        return (value)

    @property
    def height(self):
        """retrieves the height of the rectangle"""
        return (self._Rectangle__height)

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle with a value."""
        self.__validate_non_negative_integer("height", value)
        self._Rectangle__height = value
        return (value)

    @property
    def x(self):
        """retrieves the x of the rectangle"""
        return (self._Rectangle__x)

    @x.setter
    def x(self, value):
        """Sets the x of the rectangle with a value."""
        self.__validate_non_negative_integer("x", value)
        self._Rectangle__x = value
        return (value)

    @property
    def y(self):
        """retrieves the y of the rectangle"""
        return (self._Rectangle__y)

    @y.setter
    def y(self, value):
        """Sets the y of the rectangle with a value."""
        self.__validate_non_negative_integer("y", value)
        self._Rectangle__y = value
        return (value)

    def __validate_non_negative_integer(self, name, value):
        """Validates that the value is a non-negative integer."""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            if (name == "width" or name == "height"):
                raise ValueError(f"{name} must be > 0")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """Returns the area of the rectangle"""
        return (self.width * self.height)

    def display(self):
        """Displays a rectangle using a combination of '#'"""
        if (self.y > 0):
            print("\n".join(["" for _ in range(self.y)]))
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns a string literal of the class"""
        return (f"[Rectangle] ({self.id:d}) {self.x:d}/{self.y:d} \
- {self.width}/{self.height}")
