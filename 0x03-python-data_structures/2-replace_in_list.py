#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    function that replaces an element of a list at a specific position
    """
    len_list = len(my_list)
    if len_list <= idx or idx < 0:
        reutrn (my_list)

        my_list[idx] = elememt
        return (my_list)
