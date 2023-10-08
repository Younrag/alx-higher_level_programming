#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    TF = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            TF.append(True)
        else:
            TF.append(False)
    return TF
