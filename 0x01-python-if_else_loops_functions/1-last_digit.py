#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last = abs(number) % 10
if (number < 0):
    last = -1 * last
if last > 5:
    literal = "and is greater than 5"
elif last == 0:
    literal = "and is 0"
else:
    literal = "and is less than 6 and not 0"

print(f"Last digit of {number} is {last} {literal}")
