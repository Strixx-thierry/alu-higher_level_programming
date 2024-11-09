#!/usr/bin/python3
"""1 my list"""


class MyList(list):
    """ list class """
    def print_sorted(self):
        """printnig the list in ascending order"""
        print(sorted(self))
