#!/usr/bin/python3
def no_c(my_string):
    if my_string[:]:
        up_c = my_string.translate({ord("C"): None})
        low_c = up_c.translate({ord("c"): None})
        return (low_c)
    return (my_string)
