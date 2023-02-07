#!/usr/bin/python3
for soft in range(ord('a'), ord('z') + 1):
    if chr(soft) != 'q' and chr(soft) != 'e':
        print("{}".format(chr(soft)), end="")
