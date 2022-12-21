#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for j in range(x):
        try:
            print("{:d}".format(my_list[j]), end="")
            count += 1
        except(TypeError, ValueError):
            pass
        print()
        return count

"""Test"""
my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))
