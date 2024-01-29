#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for el in range(len(new_list)):
        if new_list[el] == search:
            new_list[el] = replace
    return new_list
