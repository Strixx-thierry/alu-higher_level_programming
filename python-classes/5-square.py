#!/usr/bin/python3


"""Defines a class Square with a private instance attribute size."""

class Square:

    def __init__(self, size):

        """init square"""

        self.size = size

    @property
    def size(self):

        """get the current size of square"""
        return self.__size

    @size.setter
    def size(self, value):



        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):

        return self.__size ** 2

    def my_print(self):
        """printing function  """

        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
