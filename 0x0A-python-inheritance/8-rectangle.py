#!/usr/bin/python3
"""Module for creating an empty class, with a strange method."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits 4rm BaseGeometry class"""

    def __init__(self, width, height):
        """Initialisation of the Rectangle class."""
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._Rectangle__height = height
        self._Rectangle__width = width
