#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    function that adds all unique integers
    in a list (only once for each integer).
    """
    return (sum({ele for ele in my_list}))
