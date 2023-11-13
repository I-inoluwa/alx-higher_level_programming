#!/usr/bin/python3
"""Module for creating an empty class, with a strange method."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creates a Square class that inherits directly 4rm the Rectangle class"""

    def __init__(self, size):
        """Different Initialisation of the square objects"""
        super().__init__()
        self.integer_validator("size", size)
        self._Square__size = size
        self._Rectangle__height = size
        self._Rectangle__width = size
