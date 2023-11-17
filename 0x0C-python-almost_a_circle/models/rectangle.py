#!/usr/bin/python3
"""Module Documentation: Creates a rectangle. Inherits from base"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class created, to inherit from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialisation of the Rectangle class"""
        super().__init__(id=id)
        if (type(width) != int) or (type(height) != int):
            raise TypeError("All arguments must be of integer type")

        if (type(x) != int) or (type(y) != int):
            raise TypeError("All arguments must be of integer type")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """retrieves the width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle with a value."""
        self.__validate_non_negative_integer(self, "width", value)
        self.__width = value
        return (value)

    @property
    def height(self):
        """retrieves the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle with a value."""
        self.__validate_non_negative_integer(self, "height", value)
        self.__height = value
        return (value)

    @property
    def x(self):
        """retrieves the x of the rectangle"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Sets the x of the rectangle with a value."""
        self.__validate_non_negative_integer(self, "x", value)
        self.__x = value
        return (value)

    @property
    def y(self):
        """retrieves the y of the rectangle"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Sets the y of the rectangle with a value."""
        self.__validate_non_negative_integer(self, "y", value)
        self.__y = value
        return (value)

    def __validate_non_negative_integer(self, name, value):
        """Validates that the value is a non-negative integer."""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")
