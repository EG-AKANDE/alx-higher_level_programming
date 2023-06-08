#!/usr/bin/python3

def pow(a, b):
    outcome = 1
    if b < 0:
        a = 1 / a
        b *= -1
    while b > 0:
        if (b & 1) == 1: 
            outcome *= a
        a *= a
        b >>= 1
    return outcome
