"""
Assignment 4 Problem 3: find only fuzzy matches
September 27, 2023
Vignesh Kumar Venkateshwar
"""
from string import *

def fuzzyMatching(subOne, subTwo, len_sub_str_One):
    """
    Purpose: Find fuzzy matches
    Arguments: subOne (tuple of matching start positions of sub_string1), 
               subTwo(tuple of matching start positions of sub-string 2) and len_sub_str_One (length of first sub-string)
    Return: Tuple of all fuzzy matches or -1
    """
    if len(subOne) == 0 or len(subTwo) == 0:                        # Check if one or both the tuples are empty
        return -1
    sum_pos = []                                                    # Initialize sum_pos to an empty list
    fuzzy_matches = []                                              # Initialize fuzzy_matches to an empty list
    for pos in subOne:
        sum_pos.append(pos + len_sub_str_One + 1)                   # Append pos (position) into the list
    
    for i in range(len(sum_pos)):
        for j in range(len(subTwo)):
            if sum_pos[i] == subTwo[j]:
                fuzzy_matches.append(i)
                break
    
    return tuple(fuzzy_matches)                                     # Return fuzzy_matches as a tuple


# Main program for debugging
"""
a = (0, 7, 9)
b = (2, )
len_a = len('a')
print(fuzzyMatching(a, b, len_a))
"""