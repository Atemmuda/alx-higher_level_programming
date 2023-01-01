#!/usr/bin/python3

"""
Module containing a function to add two integers

This module must be inported before used

For the doctest:
    python3 -m doctest -v tests/0-add_integer.txt
"""

def add_integer(a, b=98):
    """_summary_

    Args:
        a (int): first value
        b (int, optional): second parameter. Defaults to 98.

    Raises:
        TypeError: If the values of either a or b is not an int
        ValueError: If either 'a' or 'b' is not the proper value
        OverflowError: if the resultant value is out of range of float

    Returns:
        int: Sum of the integer value of `a` and `b`
    """
    
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) == float('nan') or type(b) == float('nan'):
         raise ValueError("cannot convert float NaN to integer")
     
    result = a + b
    if result == float('inf') or result == -float('inf'):
        raise OverflowError
    
    return int(a) + int(b)
