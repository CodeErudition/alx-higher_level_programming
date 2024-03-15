#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    all_name = dir()
    for indx in range(len(all_name)):
        if all_name[indx][:2] != "__":
            print("{:s}".format(all_name[indx]))
