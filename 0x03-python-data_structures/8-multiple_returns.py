#!/usr/bin/python3
# 8-multiple_returns.py


def multiple_returns(sentence):
    """produces str len and xtr one"""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
