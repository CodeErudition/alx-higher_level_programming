#!/usr/bin/python3
"""
This module defines a script that adds all arguments to a
Python list, and then save them to a file
"""
import sys
from os.path import exists

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

f_name = "add_item.json"

if exists(f_name):
    items = load_from_json_file(f_name)
else:
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, f_name)
