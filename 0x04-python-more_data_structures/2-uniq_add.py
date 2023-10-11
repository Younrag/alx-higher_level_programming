#!/usr/bin/python3
def uniq_add(my_list=[]):
    L = set(my_list)
    summ = 0
    for i in L:
        summ += i
    return summ
