#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    function that returns the weighted average
    of all integers tuple (<score>, <weight>)
    """
    if len(my_list) == 0:
        return 0
    result = [scores*weight for (scores, weight) in my_list]
    return sum(result) / sum([weight for (scores, weight) in my_list])
