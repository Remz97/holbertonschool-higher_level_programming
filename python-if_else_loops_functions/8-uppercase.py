#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord('A') <= ord(c) <= ord('Z'):
            print("{}".format(c), end="")
    print()
