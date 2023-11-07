#!/usr/bin/python3
"""Module for checking if the class of an object is a subclass of another"""


def inherits_from(obj, a_class):
    """Function to check if the class of an object inherits another"""

    if (issubclass(type(obj), a_class)):
        return (True)
    return (False)
