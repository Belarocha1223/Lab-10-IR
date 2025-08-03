# https://github.com/Belarocha1223/Lab-10-IR

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    pass

# https://github.com/Belarocha1223/Lab 10-IR
# Partner 1: Isabela Rocha
# Partner 2: none

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot compute square root of a negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def log(a, b):
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Invalid input for logarithm")
    return math.log(a, b)

def exp(a, b):
    return a ** b



