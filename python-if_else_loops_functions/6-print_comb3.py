#!/usr/bin/python3
for digit1 in range(10):
    for digit2 in range(digit1+1, 10):
        if digit1 == 8 and digit2 == 9:
            print('89')
        else:
            print("{:d}{:d}".format(digit1, digit2), end=", ")
