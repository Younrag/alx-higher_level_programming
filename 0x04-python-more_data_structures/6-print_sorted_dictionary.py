#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    L = list(a_dictionary.keys())
    L.sort()
    for i in L:
        print("{}: {}".format(i, a_dictionary.get(i)))
