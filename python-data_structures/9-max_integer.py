#!/usr/bin/python3
def max_integer(my_list=[]):
    for num in my_list:
        my_list.sort()
        if my_list == 0:
            return None
    print("Max: {:d}".format(my_list[-1]))
