#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """show ints in reverse"""
    if isinstance(my_list, list):
        my_list.reverse()
        for q in my_list:
            print("{:d}".format(q))
