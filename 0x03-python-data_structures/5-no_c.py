#!/usr/bin/python3

def no_c(my_string):
    """
    Function that removes all characters of 'c' & 'C' from string
    """
    new_str = my_string.translate({ord(i): None for i in 'cC'})
    return new_str
