#!/usr/bin/python3
"""Magic class creation. The only cool task on here"""


import math


class MagicClass:
    """MagicClass: Writing a class from its bytecode.

    Attributes:
        radius: Specifies the radius of the MagicObject
    """

    def __init__(self, radius=0):
        """I have to put in this documentation too.

        Attributes:
            radius: Specifies the radius of MagicObject.
        """

        self._MagicClass__radius = 0
        if ((type(radius) is not int) and (type(radius) is not float)):
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Derives the area from the radius given, or something"""

        return ((self._MagicClass__radius ** 2) * math.pi)

    def circumference(self):
        """Derives the circumference from the radius given"""

        return ((2 * math.pi) * self._MagicClass__radius)
