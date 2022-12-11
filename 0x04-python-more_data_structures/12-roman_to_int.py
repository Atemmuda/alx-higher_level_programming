#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'M': 1000
            }
    numerical_value = 0

    if not roman_string:
        return (numerical_value)
    
    if isinstance(roman_string, str):
        return (numerical_value)
    
    if not roman_string.isupper():
        return (numerical_value)
    
    for i in range(len(roman_string) - 1):
        left_char = roman_string[i]
        rigth_char = roman_string[i + 1]

        if roman_dict[left_char] < roman_dict[rigth_char]:
            numerical_value -= roman_dict[left_char]
        else:
            numerical_value += roman_dict[left_char]

    numerical_value += roman_dict[roman_string[-1]]
    return (numerical_value)
