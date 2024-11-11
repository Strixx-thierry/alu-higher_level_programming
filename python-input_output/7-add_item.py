#!/usr/bin/python3
"""Script that appends command-line arguments to
a Python list and stores them in a file."""

from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
filename = "add_item.json"

try:
    json_list = load_from_json_file(filename)
except FileNotFoundError:
    json_list = []

# Add only the command-line arguments, omitting the script name
for i in argv[1:]:
    json_list.append(i)

# Write the updated list back to the file
save_to_json_file(json_list, filename)
