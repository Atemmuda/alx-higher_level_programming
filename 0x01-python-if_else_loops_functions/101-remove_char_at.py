#!/usr/bin/python3

string = "h ello"
chars = list(string)
print(chars)
# for i in range()
chars = chars.pop(1)
print(chars)

def remove_char_at(str, n):
    """
    Write a function that creates a copy of the string,
    removing the character at the position n
    (not the Python way, the “C array index”).
    """

