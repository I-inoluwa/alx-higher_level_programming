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
