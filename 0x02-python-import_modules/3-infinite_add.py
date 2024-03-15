#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    x = len(argv)
    sum_args = 0
    for indx in range(1, x):
        sum_args += int(argv[indx])
    print("{}".format(sum_args))
