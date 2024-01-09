#!/usr/bin/python3
"""This is the documentation for the module. Necessary"""


class Student:
    """Creation of a Student class, with some attributes"""

    def __init__(self, first_name, last_name, age):
        """Initialiser of an instance of the Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Public method that retrives a dict repr of a Student instance"""
        serial = {}
        for each in vars(self):
            serial[each] = self.__getattribute__(each)

        return serial
