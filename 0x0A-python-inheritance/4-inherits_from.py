#!/usr/bin/python3
"""Module for checking if the class of an object is a subclass of another"""


def inherits_from(obj, a_class):
    """Function to check if the class of an object inherits another"""

    for each in obj.__class__.mro()[1:]:
        if issubclass(each, a_class):
            return True
    return False
