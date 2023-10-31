#!/usr/bin/python3
# Author - Tolulope Fakunle
"""Print the numbers from 1 to 100 separated by a space.
  For multiples of three, print Fizz instead of the number
  For multiples of five, print Buzz instead of the number.
  For multiples of three and five, print FizzBuzz instead of the number.
  """


def fizzbuzz():
    for w in range(1, 101):
        if w % 3 == 0 and w % 5 == 0:
            print("FizzBuzz ", end="")
        elif w % 3 == 0:
            print("Fizz ", end="")
        elif w % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(w), end="")
