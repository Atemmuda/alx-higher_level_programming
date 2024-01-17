#!/usr/bin/python3
"""Adds unique element in a list -- using sets"""
def uniq_add(my_list=[]):
    result = 0
    my_set = set(my_list)
    for i in my_set:
        result += my_set[i]
    return (result)

