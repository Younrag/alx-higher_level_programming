#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    c = number % 10
    if c > 5:
        print('Last digit of', number, 'is', c, 'and is greater than 5')
    elif c == 0:
        print('Last digit of', number, 'is', c, 'and is 0')
    else:
        print('Last digit of', number, 'is', c, 'and is less than 6 and not 0')
else:
    c = -number % 10
    print('Last digit of', number, 'is', -c, 'and is less than 6 and not 0')
