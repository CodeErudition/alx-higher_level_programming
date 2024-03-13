#!/usr/bin/python3

def remove_char_at(_str, n):
    if n < 0:
        return (_str)
    return (_str[:n] + _str[n+1:])
