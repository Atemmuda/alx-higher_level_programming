#!/usr/bin/python3
"""
Module for printing square of pound (#)

Sholud be used as a module 
"""

# Prototype: def print_square(size):
# size is the size length of the square
# size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
# if size is less than 0, raise a ValueError exception with the message size must be >= 0
# if size is a float and is less than 0, raise a TypeError exception with the message size must be an integer

def print_square(size):
    """This funtion print a square of pound sign (#) of the size passed to it

    Args:
        size (int): length and breath of teh sqare to be printed
    
    Retruns: None
    
    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is less than 0.
    """
    if type(size) is float and size != round(size):
        raise TypeError("size must be an integer")
    if type(size) is not int and type(size) is not float:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size >= 0:
        size = round(size)
    for i in range(size):
        print("#"*size)
