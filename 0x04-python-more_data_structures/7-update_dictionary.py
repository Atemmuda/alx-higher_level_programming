#!/usr/bin/python3
"""Update a dictionary with the key and value provided,
if the key is in dictionary, change the value to parameter value
else add the new key,value pairs"""

def update_dictionary(a_dictionary, key, value):
    for k, v in a_dictionary.items():
        if k == key:
            a_dictionary[k] = value
            break;
        else:
            a_dictionary[key] = value
    return (a_dictionary)
