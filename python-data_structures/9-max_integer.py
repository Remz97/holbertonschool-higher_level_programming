#!/usr/bin/python3
def max_integer(my_list=[]):
        for num in my_list:
            if len(my_list) == 0:
              return None
            else:
                my_list.sort()
        print("Max: {:d}".format(my_list[-1]))


my_list = [0, 9, 7]
max_value = max_integer(my_list)