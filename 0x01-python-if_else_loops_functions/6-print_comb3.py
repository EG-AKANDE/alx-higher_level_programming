#!/usr/bin/python3

for q in range(10):
    for r in range(q + 1, 10):
        print("{:d}{:d}".format(q, r), end=", " if q != 8 or r != 9 else "\n")
