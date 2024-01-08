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
