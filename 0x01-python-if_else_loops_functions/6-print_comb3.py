#!/usr/bin/python3
for i in range(10):
    for j in range(i+1, 10):
        if i != j:
            print("{:d}{:d}".format(i, j), end=", " if (i < 8 or (i == 8 and j == 9)) else "")
print() # Add a newline character at the end