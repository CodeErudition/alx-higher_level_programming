#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    x = len(argv) - 1
    if x < 1:
        print("{} argument.".format(x))
    elif x == 1:
        print("{} argument:".format(x))
    else:
        print("{} arguments:".format(x))
    for indx in range(1, x + 1):
        print("{}: {:s}".format(indx, argv[indx])) 
