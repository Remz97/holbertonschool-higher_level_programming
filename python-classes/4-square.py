#!/usr/bin/python3
'''
add a private instance attribute: size
'''


class Square():
    '''
    adding a private instance attribute: size
    '''
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Get size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        '''Initializes the data'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''returns the current square'''
        return self.__size * self.__size
