#!/usr/bin/python3
"""This documentation is very necessary"""


class MyInt(int):
    """An inherited class of int. with some methods inverted"""

    def __eq__(self, __value: object):
        """Inverts it with not equals"""
        return super().__ne__(__value)

    def __ne__(self, __value: object):
        """Inverts it with equals"""
        return super().__eq__(__value)
