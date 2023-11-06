#!/usr/bin/python3
def element_at(my_list, idx):
    """
    function that retrieves an element from a list
    """
    len_list = len(my_list)
    if idx >= len_list or idx < 0:
        return

    return (my_list[idx])
