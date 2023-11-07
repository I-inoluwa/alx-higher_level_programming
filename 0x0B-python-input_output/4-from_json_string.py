#!/usr/bin/python3
"""This is the documentation for the module. Necessary"""


import json


def from_json_string(my_str):
    """Function that returns the object from a JSON representation"""
    return (json.loads(my_str))
