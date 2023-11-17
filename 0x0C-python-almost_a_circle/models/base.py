#!/usr/bin/python3
"""Module Documentation: Base file for all other models"""


import json


class Base:
    """Base class. All other classes inherit from this."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation of the base class"""
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Converts a dictionary to JSON string"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"
