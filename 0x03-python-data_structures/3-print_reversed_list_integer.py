#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in reversed(range(0, len(my_list))):
        if isinstance(my_list[i], int):
            print("{:d}".format(my_list[i]))
