#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        l_digit = number % -10
        print(-(l_digit), end="")
    else:
        l_digit = number % 10
        print(l_digit, end="")
    return abs(l_digit)
