#!/usr/bin/python3
def weight_average(my_list=[]):
    summation = 0
    weighted_average
    count = 0
    if not my_list:
        return (0)
    else:
        for (value, weight) in my_list:
            summation = summation + (value * weight)
            count += weight
    weighted_average = summation / count
    return (weighted_average)
