#!/usr/bin/python3
def best_score(a_dictionary):
    best_score = 0
    if not a_dictionary:
        return None
    for key, v in a_dictionary.items():
        if v > best_score:
            best_score = v
            return (key)
