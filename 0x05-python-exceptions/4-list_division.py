#!/bin/usr/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except TypeError:
            res = 0
            print("wrong type")
        except ZeroDivisionError:
            res = 0
            print("division by zero")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            result.append(res)
    return result
