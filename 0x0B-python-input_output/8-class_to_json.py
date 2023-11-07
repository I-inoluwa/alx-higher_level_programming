#!/usr/bin/python3
"""This is the documentation for the module. Necessary"""


def class_to_json(obj):
    """Returns the dictionary description for JSON of an object"""
    serial = {}
    for each in dir(obj):
        serial[each] = obj.__getattribute__(each)
    return serial

class MyClass:
    """ My class
    """

    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)
    
m = MyClass("John")
m.number = 89
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)
