#!/usr/bin/python3

def uniq_add(my_list=[]):
	u_list = set()
	if my_list:
		for i in my_list:
			u_list.add(i)
	return sum(u_list)
