#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


def is_kind_of_class(obj, a_class):
    """Check if the object is an instance or if the object is an instance of a class that inherited from"""
    return isinstance(obj, a_class)
