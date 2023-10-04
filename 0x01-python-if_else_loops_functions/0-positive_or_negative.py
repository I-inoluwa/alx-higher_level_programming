#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if (number < 0):
        literal = "is negative"
elif (number > 0):
        literal = "is positive"
else:
        literal = "is zero"

print(f"{number} {literal}");
