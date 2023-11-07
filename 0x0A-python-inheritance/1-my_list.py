#!/usr/bin/python3
"""This documentation is always important"""


class MyList(list):
    """A new class that inherits from python's inherent list"""

    def print_sorted(self):
        """Function that prints a list in its sorted form"""
        print(sorted(self))
