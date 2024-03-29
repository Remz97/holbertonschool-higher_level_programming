#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a specified class"""
    return type(obj) is a_class
