#!/usr/bin/python3
for i in range(97, 123):
    n = 219 - i
    if i % 2 == 0:
        n = n - 32
    print("{:c}".format(n), end='')
