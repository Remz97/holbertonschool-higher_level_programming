#!/usr/bin/python3
'''
add a private instance attribute: size
'''


class Square():
    '''
    adding a private instance attribute: size
    '''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        for i in range(self.__size):
            for j in range(self.__size):
                return self.__size * self.__size
