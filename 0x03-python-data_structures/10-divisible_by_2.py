#!/usr/bin/python3
# 10-divisible_by_2.py


def divisible_by_2(my_list=[]):
    """2 multiples"""
    multiples = []
    for q in range(len(my_list)):
        if my_list[q] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return (multiples)
