#!/usr/bin/python3
"""This documentation is very necessary"""


def add_attribute(obj, name, value):
    """Adds attribute to an instnace of a class, if possible"""
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
