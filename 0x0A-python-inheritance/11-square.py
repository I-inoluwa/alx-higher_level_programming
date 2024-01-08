#!/usr/bin/python3
"""Module for creating an empty class, with a strange method."""


class BaseGeometry:
    """Empty BaseGeometry class. Area method is added."""

    def __init__(self):
        """Initialization of an instance of a class"""
        pass

    def area(self):
        """Class method for finding the area of an object"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Class method for validating a specific attribute"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class that inherits 4rm BaseGeometry class"""

    def __init__(self, width, height):
        """Initialisation of the Rectangle class."""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._Rectangle__height = height
        self._Rectangle__width = width

    def area(self):
        """Area is now being implemented"""

        return (self._Rectangle__height * self._Rectangle__width)

    def __str__(self):
        """A string representation of rectangle object"""
        w = self._Rectangle__width
        h = self._Rectangle__height
        return ("[Rectangle] {}/{}".format(w, h))


class Square(Rectangle):
    """Creates a Square class that inherits directly 4rm the Rectangle class"""

    def __init__(self, size):
        """Different Initialisation of the square objects"""
        self.integer_validator("size", size)
        self._Square__size = size
        self._Rectangle__height = size
        self._Rectangle__width = size

    def __str__(self):
        """A string representation of square object"""
        w = self._Rectangle__width
        h = self._Rectangle__height
        return ("[Square] {}/{}".format(w, h))
