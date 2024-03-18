#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for out in matrix:
            for inn in out:
                print("{:d}".format(inn), end=" " if inn != out[-1] else "")
            print()
