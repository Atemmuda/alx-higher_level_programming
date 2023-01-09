#!/usr/bin/python3
"""Module containing function to print string
by line. It contains no directly executable code
It should be imported as a module
"""

def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be string")
    delimeters = '?.:'
    for c in delimeters:
        text = str(c +'\n\n'.join(s.strip() for s in text.split(c)))
    print(text, end='')
    if len(text) > 0 and text[-1] in delimeters:
        print('\n')

