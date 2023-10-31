#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastnumb = number % -10
elif number >= 0:
    lastnumb = number % 10
if lastnumb > 5:
    print(f"Last digit of {number} is {lastnumb} and is greater than 5")
elif lastnumber == 0:
    print(f"Last digit of {number} is {lastnumb} and is 0")
else:
    print(f"Last digit of {number} is {lastnumb} and is less than 6 and not 0")
