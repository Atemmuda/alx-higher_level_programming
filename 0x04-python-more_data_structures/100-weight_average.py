#!/usr/bin/python3
def weight_average(my_list=[]):
    summation = 0
    count = 0
    if my_list:
        for (value, weight) in my_list:
            summation = summation + (value * weight)
            count += weight
        weighted_average = summation / count
        return (weighted_average)
    else:
        return (0)
