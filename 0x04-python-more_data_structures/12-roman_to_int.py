#!/usr/bin/python3
from functools import reduce


def roman_to_int(roman_string):
    if (type(roman_string) == str):
        cache = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        track = [10000]
        for each in roman_string.upper():
            # track.append(cache[each])
            if (track[-1] < cache[each]):
                track[-1] = cache[each] - track[-1]
            else:
                track.append(cache[each])

        result = reduce(lambda x, y: x + y, track[1:])
        return (result)
    return (0)
