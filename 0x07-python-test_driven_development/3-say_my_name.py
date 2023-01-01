#!/usr/bin/python3
"""
Module containig funtion for printing ``My name is first_name  last_name``

Should be imported before used
"""

def say_my_name(first_name, last_name=""):
    """THis function prints ``My name is 'first_name last_name'``

    Args:
        first_name (str): First name to use
        last_name (str, optional): last name to be used. Defaults to "".

    Raises:
        ValueError: if first_name is an empty string
        TypeError: if first_name is not a string
        TypeError: if last_name is not a string

    Returns:
        _type_: _description_
    """
    if first_name == "":
        raise ValueError("first_name cannot be an empty string")
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
