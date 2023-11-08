#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """
    function that deletes keys with a specific value in a dictionary.
    """
    if a_dictionary is not None and type(a_dictionary) is dict:
        elements = a_dictionary.items()
        to_delete = {key: val for (key, val) in elements if value == val}
        for (key, val) in to_delete.items():
            del a_dictionary[key]
        return a_dictionary.copy()
