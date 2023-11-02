#!/usr/bin/python3
from magic_calculation_102 import add, sub

def magic_calculation(a, b):
    if a < b:
        return add(add(a, b), sum(range(4, 6)))
    return sub(a, b)
