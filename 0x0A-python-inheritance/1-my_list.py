#!/usr/bin/python3
"""This documentation is always neccessary"""


class MyList(list):
    """A new class that inherits the python's inherent list"""

    def __init__(self) -> None:
        return super().__init__()

    def print_sorted(self):
        """Function that prints a list in its sorted form"""
        print(sorted(self))
