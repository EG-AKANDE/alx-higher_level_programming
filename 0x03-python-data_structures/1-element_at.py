#!/usr/bin/python3
# 1-element_at.py


def element_at(my_list, idx):
    """pull element 4rm list"""
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return (my_list[idx])