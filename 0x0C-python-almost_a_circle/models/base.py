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
        if list_objs:
            for each in list_objs:
                arr.append(each.to_dictionary())
        json_repr = cls.to_json_string(arr)

        filename = f"{str(cls).split('.')[2][:-2]}.json"
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write(json_repr)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation."""
        if json_string:
            return (json.loads(json_string))
        return ([])

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all the attributes already set"""
        if str(cls).split('.')[2][:-2] == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)

        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = f"{str(cls).split('.')[2][:-2]}.json"
        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            return []

        arr = cls.from_json_string(content)
        instance_out = []
        for each in arr:
            instance_out.append(cls.create(**each))

        return instance_out
