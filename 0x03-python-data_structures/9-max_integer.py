#!/usr/bin/python3
# 9-max_integer.py


def max_integer(my_list=[]):
    """biggest int"""
    if len(my_list) == 0:
        return (None)

    big = my_list[0]
    for q in range(len(my_list)):
        if my_list[q] > big:
            big = my_list[q]

    return (big)
