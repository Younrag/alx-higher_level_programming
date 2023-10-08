#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    l = my_list[0]
    for i in range(1, len(my_list)):
        if l < my_list[i]:
            l = my_list[i]
    return l
