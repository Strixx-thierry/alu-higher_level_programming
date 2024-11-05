#!/usr/bin/python3


"""Square module"""


class Square:
    """ define class"""

    def __init__(self, size):

        """initalize  square"""

        self.size = size

    @property
    def size(self):

        """get the current size square decoration"""
        return self.__size

    @size.setter
    def size(self, value):

        """check for errors """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ calculate  the area of the square"""

        return self.__size ** 2

    def my_print(self):
        """print the funtion of """

        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
