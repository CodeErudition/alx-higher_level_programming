#!/usr/bin/python3

for chars in range(97, 123):
    if chars == 101 or chars == 113:
        continue
    print("{}".format(chr(chars)), end="")
