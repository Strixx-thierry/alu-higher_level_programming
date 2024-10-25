#!/usr/bin/python3
def search_replace(list_1, search, replace):
    return [replace if x == search else x for x in list_1]
