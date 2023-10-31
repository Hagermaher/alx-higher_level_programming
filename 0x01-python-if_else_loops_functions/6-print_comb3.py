#!/usr/bin/python3
# Author - Tolulope Fakunle

for dgt1 in range(0, 10):
    for dgt2 in range(digit1 + 1, 10):
        if dgt1 == 8 and dgt2 == 9:
            print("{}{}".format(dgt1, dgt2))
        else:
            print("{}{}".format(dgt1, dgt2), end=", ")
