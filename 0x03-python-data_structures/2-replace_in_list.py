#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx in range(0, len(my_list)):
        del my_list[idx]
        my_list.insert(idx, element)
        return my_list
    return my_list
