#!/usr/bin/python3
"""Task 6 - 0x10. Python - Network #0"""


def find_peak(list_of_integers):
    """
    function that finds a peak in a list of unsorted integers.
    """
    
    if list_of_integers == [None]:
        return None
    peak = 0
    if list_of_integers[0] >= list_of_integers[1]:
        peak = list_of_integers[0]
    elif list_of_integers[-1] >= list_of_integers[-2]:
        peak = list_of_integers[-1]
    else:
        for i in range(1, (len(list_of_integers) - 1)):
            if list_of_integers[i] >= list_of_integers[i - 1] and list_of_integers[i] >= list_of_integers[i + 1]:
                peak = list_of_integers[i]
    return peak
