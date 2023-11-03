#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for u in range(len(matrix)):
        for g in range(len(matrix[u])):
            print("{:d}".format(matrix[u][g]), end="")
            if g != (len(matrix[u]) - 1):
                print(" ", end="")

        print("")
