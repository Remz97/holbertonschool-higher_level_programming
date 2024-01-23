#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if 'A' <= c <= 'Z':
            print("{}".format(chr(ord(c))), end="")
        else:
            print("{}".format(c), end="")
    print()
