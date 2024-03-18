#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n_list = my_list[:]
    if idx < 0:
        return (my_list)
    if idx > len(my_list) - 1:
        return (my_list)
    n_list[idx] = element
    return (n_list)
