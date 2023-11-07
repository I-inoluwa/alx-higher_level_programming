#!/usr/bin/python3
"""This is the documentation for the module. Necessary"""


def class_to_json(obj):
    """Returns the dictionary description for JSON of an object"""
    serial = {}
    for each in vars(obj):
        serial[each] = obj.__getattribute__(each)
    return serial
