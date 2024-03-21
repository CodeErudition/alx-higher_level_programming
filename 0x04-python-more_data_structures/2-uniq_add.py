#!/usr/bin/python3

def uniq_add(my_list=[]):
	u_list = set(my_list)
	sum_i = 0
	for i in u_list:
		sum_i += i
	return (sum_i)
