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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a dictionary to JSON string"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string repr of list_objs to a file"""
        arr = []
        for each in list_objs:
            arr.append(each.to_dictionary())
        json_repr = cls.to_json_string(arr)

        filename = f"{str(list_objs[0]).split()[0][1:-1]}.json"
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write(json_repr)
