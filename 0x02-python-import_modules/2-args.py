#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    x = len(argv) - 1
    if x == 0:
        print("{} arguments.".format(x))
    elif x == 1:
        print("{} argument:".format(x))
    else:
        print("{} arguments:".format(x))
    for indx in range(count):
        print("{}: {}".format(indx + 1, argv[indx + 1]))
