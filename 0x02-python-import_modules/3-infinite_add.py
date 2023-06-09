#!/usr/bin/python3

if __name__ == "__main__":
    """gives all args sum."""
    import sys

    total = 0
    for u in range(len(sys.argv) - 1):
        total += int(sys.argv[u + 1])
    print("{}".format(total))
