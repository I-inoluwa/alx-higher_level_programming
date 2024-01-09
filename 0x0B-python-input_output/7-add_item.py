#!/usr/bin/python3
"""This is the documentation for the module. Necessary"""


import json
import sys


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using JSON representation"""
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """Creates an Object from a JSON file"""
    with open(filename, mode='r', encoding='utf-8') as f:
        return (json.load(f))


def load_add_save(filename):
    """Adds each command line argument to a JSON list in a file"""
    args = sys.argv[1:]
    try:
        arr = load_from_json_file(filename)
    except Exception:
        arr = []

    arr.extend(args)
    save_to_json_file(arr, filename)


load_add_save("add_item.json")
